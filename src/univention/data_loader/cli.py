#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2023 Univention GmbH


import logging
from typing import Annotated, List, Optional

import typer
import yaml

from univention.admin.rest.client import UDM

from . import process_template

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
    process_template.run(
        udm,
        input_filename,
        template_context=context,
        template_extension=template_extension,
        log_template=log_template,
    )


def read_from_file(filename):
    with open(filename, "r") as input_file:
        content = input_file.read()
    return content


def load_and_merge_contexts(filenames: list[str]) -> dict:
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


def _connect_to_udm(udm_api_url, udm_api_user, udm_api_password_file):
    log.info("Connecting to UDM API at URL %s", udm_api_url)
    udm_api_password = read_from_file(udm_api_password_file)
    udm = UDM.http(udm_api_url, udm_api_user, udm_api_password)
    return udm


def run():
    cli_app(standalone_mode=False)


if __name__ == "__main__":
    run()
