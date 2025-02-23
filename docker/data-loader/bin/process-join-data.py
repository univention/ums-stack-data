#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


import logging
from typing import Annotated, List, Optional

import typer
import yaml
from jinja2 import StrictUndefined, Template
from univention.admin.rest.client import UDM, NotFound, UnprocessableEntity

log = logging.getLogger("app")


cli_app = typer.Typer(pretty_exceptions_enable=False)


@cli_app.command()
def main(
    input_filename: str,
    udm_api_url: Annotated[
        str,
        typer.Option(
            envvar="UDM_API_URL",
            help="URL to the UDM Rest API",
        ),
    ],
    udm_api_user: Annotated[
        str,
        typer.Option(
            envvar="UDM_API_USER",
            help="Username to use when connecting to the UDM Rest API",
        ),
    ],
    udm_api_password_file: Annotated[
        str,
        typer.Option(
            envvar="UDM_API_PASSWORD_FILE",
            help="File containing the password to connect to the UDM Rest API",
        ),
    ],
    log_context: Annotated[
        bool,
        typer.Option(help="Log the context values. This may log out sensitive data."),
    ] = False,
    log_template: Annotated[
        bool,
        typer.Option(
            help="Log the rendered template. This may log out sensitive data.",
        ),
    ] = False,
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
    logging.basicConfig(level=logging.INFO)
    log.setLevel(logging.DEBUG)

    context = load_and_merge_contexts(template_context) if template_context else {}
    if log_context:
        log.debug("Merged context\n%s", yaml.safe_dump(context))

    udm = _connect_to_udm(udm_api_url, udm_api_user, udm_api_password_file)
    app = App(
        udm,
        template_context=context,
        template_extension=template_extension,
        log_template=log_template,
    )
    app.run(input_filename)


class App:
    def __init__(
        self,
        udm,
        template_context=None,
        template_extension=None,
        log_template=False,
    ):
        self.log_template = log_template
        self.udm = udm
        self.template_context = template_context or {}
        self.template_extension = template_extension

    def run(self, input_filename):
        log.info("Processing file %s", input_filename)

        content = read_from_file(input_filename)
        if is_template(input_filename, extension=self.template_extension):
            log.info("Rendering file as Jinja2 template")
            content = render_template(content, self.template_context)
            if self.log_template:
                log.debug("Rendered template:\n%s", content)

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
        elif data["action"] == "ensure_list_does_not_contain":
            self.ensure_list_does_not_contain(
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
        elif data["action"] == "modify_if_exists":
            self.modify_if_exists(
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
            self.delete_udm_object(
                module=data["module"],
                position=data["position"],
            )
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

    def modify_if_exists(self, module, position, properties):
        log.info(f"Modifying UDM object if exists: {module}, {position}")
        try:
            obj = self.udm.obj_by_dn(position)
            log.debug(f"Updating properties {list(properties.keys())}")
            obj.properties.update(properties)
            obj.save()
        except NotFound:
            log.info(f"Object not found: {position}. No changes made.")

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

    def remove_from_list(self, module, position, properties, policies):
        log.info(f"Removing attribute from list {module}, {position}")
        obj = self.udm.obj_by_dn(position)
        needs_save = False
        needs_save |= self._remove_values_from_dict(properties, obj.properties)
        needs_save |= self._remove_values_from_dict(policies, obj.policies)
        if needs_save:
            log.info(f'Saving object "{obj.dn}".')
            obj.save()
        else:
            log.info(f'No changes made to object "{obj.dn}".')

    def ensure_list_does_not_contain(self, module, position, properties, policies):
        log.info(f"Ensuring attribute list does not contain value {module}, {position}")
        obj = self.udm.obj_by_dn(position)
        needs_save = False
        needs_save |= self._remove_values_from_dict(properties, obj.properties)
        needs_save |= self._remove_values_from_dict(policies, obj.policies)
        if needs_save:
            log.info(f'Saving object "{obj.dn}".')
            obj.save()
        else:
            log.info(f'No changes made to object "{obj.dn}".')

    def _remove_values_from_dict(self, values, obj_values):
        needs_save = False
        for name, values_list in values.items():
            log.info(f'Removing values "{values_list}" from "{name}".')
            current_values = obj_values[name]
            for value in values_list:
                if value in current_values:
                    log.debug(f'Removing value "{value}" from property "{name}".')
                    current_values.remove(value)
                    needs_save = True
                else:
                    log.debug(f'Value "{value}" not present in property "{name}".')
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
    for key, value in source.items():
        if isinstance(value, dict):
            sub_target = target.setdefault(key, {})
            deep_merge(sub_target, value)
        else:
            target[key] = value
    return target


def _connect_to_udm(udm_api_url, udm_api_user, udm_api_password_file):
    log.info("Connecting to UDM API at URL %s", udm_api_url)
    udm_api_password = read_from_file(udm_api_password_file)
    udm = UDM.http(udm_api_url, udm_api_user, udm_api_password)
    return udm


if __name__ == "__main__":
    cli_app(standalone_mode=False)
