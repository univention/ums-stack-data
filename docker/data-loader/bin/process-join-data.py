#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


import logging
import os
from typing import Annotated, List, Optional

import typer
import yaml
from jinja2 import StrictUndefined, Template
from univention.admin.rest.client import UDM, NotFound, UnprocessableEntity

log = logging.getLogger("app")


cli_app = typer.Typer()


@cli_app.command()
def main(
    input_filename: str,
    template_context: Annotated[
        Optional[List[str]],
        typer.Option(help="Load the template context from this YAML file."),
    ] = None,
    template_extension: Annotated[
        Optional[str],
        typer.Option(
            help="Restrict template processing to a specific filename extension",
        ),
    ] = None,
):
    udm = _connect_to_udm()
    context = load_and_merge_contexts(template_context) if template_context else {}
    app = App(udm, template_context=context, template_extension=template_extension)
    app.run(input_filename)


class App:
    def __init__(self, udm, template_context=None, template_extension=None):
        logging.basicConfig(level=logging.INFO)
        log.setLevel(logging.DEBUG)

        self.udm = udm
        self.template_context = template_context or {}
        self.template_extension = template_extension

    def run(self, input_filename):
        log.info("Processing file %s", input_filename)

        content = read_from_file(input_filename)
        if is_template(input_filename, extension=self.template_extension):
            log.info("Rendering file as Jinja2 template")
            content = render_template(content, self.template_context)

        actions = list(yaml.safe_load_all(content))

        for action in actions:
            self.process_action(action)

        log.info("Finished file %s", input_filename)

    def process_action(self, data):
        if data["action"] == "create":
            self.ensure_udm_object(
                module=data["module"],
                position=data["position"],
                properties=data["properties"],
            )
        elif data["action"] == "ensure_list_contains":
            self.ensure_list_contains(
                module=data["module"],
                position=data["position"],
                properties=data.get("properties", {}),
                policies=data.get("policies", {}),
            )
        elif data["action"] == "modify":
            self.update_udm_object(
                module=data["module"],
                position=data["position"],
                properties=data.get("properties"),
            )
        elif data["action"] == "create_or_modify":
            self.upsert_udm_object(
                module=data["module"],
                position=data["position"],
                properties=data.get("properties"),
            )
        elif data["action"] == "delete_if_exists":
            self.delete_udm_object(module=data["module"], position=data["position"])

        else:
            raise NotImplementedError(f"Action {data['action']} not supported.")

    def ensure_udm_object(self, module, position, properties):
        log.info(f"Ensuring udm object {module}, {position}, {properties.get('name')}")
        module_obj = self.udm.get(module)
        obj = module_obj.new(position=position)
        obj.properties.update(properties)
        try:
            obj.save()
        except UnprocessableEntity as exc:
            object_exists_message = '"dn" Object exists'
            # TODO: Find a more solid way to check if the object exists
            if object_exists_message in str(exc):
                log.info("Object does already exist, not updating anything.")
            else:
                raise

    def update_udm_object(self, module, position, properties):
        log.info(f"Updating UDM object {module}, {position}")
        obj = self.udm.obj_by_dn(position)
        log.debug(f"Updating properties {list(properties.keys())}")
        obj.properties.update(properties)
        obj.save()

    def upsert_udm_object(self, module, position, properties):
        log.info(f"Ensuring udm object {module}, {position}, {properties.get('name')}")
        module_obj = self.udm.get(module)
        obj = module_obj.new(position=position)
        obj.properties.update(properties)
        try:
            obj.save()
        except UnprocessableEntity as exc:
            object_exists_message = '"dn" Object exists'
            # TODO: Find a more solid way to check if the object exists
            if object_exists_message in str(exc):
                update_position = f"cn={properties.get('name')},{position}"
                self.update_udm_object(module, update_position, properties)
            else:
                raise

    def delete_udm_object(self, module, position):
        log.info(f"Deleting UDM object {module}, {position}")
        try:
            obj = self.udm.obj_by_dn(position)
            obj.delete()
        except NotFound:
            log.info("The object does not exist, not deleting anything.")

    def ensure_list_contains(self, module, position, properties, policies):
        log.info(f"Ensuring attribute list contains value {module}, {position}")
        obj = self.udm.obj_by_dn(position)
        needs_save = False
        needs_save |= self._ensure_values_in_dict(properties, obj.properties)
        needs_save |= self._ensure_values_in_dict(policies, obj.policies)
        if needs_save:
            log.info(f'Saving object "{obj.dn}".')
            obj.save()
        else:
            log.info(f'No changes made to object "{obj.dn}".')

    def _ensure_values_in_dict(self, values, obj_values):
        needs_save = False
        for name, values in values.items():
            log.info(
                f'Ensuring values "{values}" in "{name}".',
            )
            current_values = obj_values[name]
            for value in values:
                if value not in current_values:
                    log.debug(f'Adding value "{value}" into property "{name}".')
                    current_values.append(value)
                    needs_save = True
                else:
                    log.debug(f'Value "{value}" already present in property "{name}".')
        return needs_save


def read_from_file(filename):
    with open(filename, "r") as input_file:
        content = input_file.read()
    return content


def is_template(filename, extension=None):
    if extension:
        return filename.endswith(f".{extension}")
    return True


def render_template(content, context):
    template = Template(content, undefined=StrictUndefined)
    return template.render(context)


def load_and_merge_contexts(filenames):
    contexts = [load_context(filename) for filename in filenames]
    result = {}
    for context in contexts:
        deep_merge(result, context)
    return result


def load_context(filename):
    log.info("Reading context from file %s", filename)
    content = read_from_file(filename)
    return yaml.safe_load(content)


def deep_merge(target, source):
    target.update(source)
    return target


def _connect_to_udm():
    udm_api_url = os.environ["UDM_API_URL"]
    log.info("Connecting to UDM API at URL %s", udm_api_url)
    udm_api_user = os.environ["UDM_API_USER"]
    with open(os.environ["UDM_API_PASSWORD_FILE"], "r") as password_file:
        udm_api_password = password_file.read()
    udm = UDM.http(udm_api_url, udm_api_user, udm_api_password)
    return udm


if __name__ == "__main__":
    cli_app()
