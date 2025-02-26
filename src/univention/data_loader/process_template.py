#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


import logging

import yaml
from jinja2 import StrictUndefined, Template

from univention.admin.rest.client import UDM

from .actions import get_action_runner

log = logging.getLogger(__name__)


def run(
    udm: UDM,
    input_filename: str,
    template_context: dict | None = None,
    template_extension: str | None = None,
    log_template=False,
):
    log.info("Processing file %s", input_filename)

    content = read_from_file(input_filename)
    if is_template(input_filename, extension=template_extension):
        log.info("Rendering file as Jinja2 template")
        content = render_template(content, template_context or {})
        if log_template:
            log.debug("Rendered template:\n%s", content)

    actions = list(yaml.safe_load_all(content))

    for action in actions:
        process_action(udm, action)

    log.info("Finished file %s", input_filename)


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


def process_action(udm, data):
    action_runner = get_action_runner(data["action"])
    if not action_runner:
        raise NotImplementedError(f"Action {data['action']} not supported.")
    action_runner(
        udm,
        data["module"],
        data["position"],
        data.get("properties", {}),
        data.get("policies", {}),
    )
