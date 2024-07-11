from unittest import mock

import pytest
from typer.testing import CliRunner

runner = CliRunner()


def test_shows_help_information(process_join_data):
    result = runner.invoke(process_join_data.cli_app, ["--help"])
    assert result.exit_code == 0


def test_accepts_filename_as_argument(process_join_data, mocker):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    run_mock = mocker.patch.object(process_join_data.App, "run")

    result = runner.invoke(process_join_data.cli_app, ["example-data.yaml"])

    run_mock.assert_called_once_with("example-data.yaml")
    assert result.exit_code == 0


def test_accepts_template_extension_as_option(process_join_data, mocker):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    app_mock = mocker.patch.object(process_join_data, "App")

    result = runner.invoke(
        process_join_data.cli_app, ["example-data.yaml", "--template-extension", ".j2"])

    assert app_mock.call_args.kwargs["template_extension"] == ".j2"
    assert result.exit_code == 0


def test_accepts_template_context_as_option(process_join_data, mocker):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    app_mock = mocker.patch.object(process_join_data, "App")
    stub_context = {"stub_name": "stub_value"}
    load_context_mock = mocker.patch.object(
        process_join_data, "load_context", return_value=stub_context)

    result = runner.invoke(
        process_join_data.cli_app, ["example-data.yaml", "--template-context", "context.yaml"])

    load_context_mock.assert_called_once_with("context.yaml")
    assert app_mock.call_args.kwargs["template_context"] == stub_context
    assert result.exit_code == 0
