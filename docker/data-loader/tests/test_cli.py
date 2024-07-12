# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024 Univention GmbH

import logging

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
        process_join_data.cli_app,
        ["example-data.yaml", "--template-extension", ".j2"],
    )

    assert app_mock.call_args.kwargs["template_extension"] == ".j2"
    assert result.exit_code == 0


def test_accepts_template_context_as_option(process_join_data, mocker):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    app_mock = mocker.patch.object(process_join_data, "App")
    stub_context = {"stub_name": "stub_value"}
    load_context_mock = mocker.patch.object(
        process_join_data,
        "load_context",
        return_value=stub_context,
    )

    result = runner.invoke(
        process_join_data.cli_app,
        ["example-data.yaml", "--template-context", "context.yaml"],
    )

    load_context_mock.assert_called_once_with("context.yaml")
    assert app_mock.call_args.kwargs["template_context"] == stub_context
    assert result.exit_code == 0


def test_accepts_multiple_template_context_options(process_join_data, mocker):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    app_mock = mocker.patch.object(process_join_data, "App")
    stub_context = {"stub_name": "stub_value"}
    stub_context2 = {"stub_name2": "stub_value2"}
    mocker.patch.object(
        process_join_data,
        "load_context",
        side_effect=[stub_context, stub_context2],
    )

    result = runner.invoke(
        process_join_data.cli_app,
        [
            "example-data.yaml",
            "--template-context",
            "context.yaml",
            "--template-context",
            "context2.yaml",
        ],
    )

    expected_context = stub_context | stub_context2
    assert app_mock.call_args.kwargs["template_context"] == expected_context
    assert result.exit_code == 0


def test_does_not_log_context_by_default(process_join_data, mocker, caplog):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    stub_context = {"stub_name": "stub_value"}
    stub_context2 = {"stub_name2": "stub_value2"}
    mocker.patch.object(
        process_join_data,
        "load_context",
        side_effect=[stub_context, stub_context2],
    )

    with caplog.at_level(logging.DEBUG, logger="app"):
        result = runner.invoke(
            process_join_data.cli_app,
            [
                "example-data.yaml",
                "--template-context",
                "context.yaml",
                "--template-context",
                "context2.yaml",
            ],
        )

    assert "Merged context" not in caplog.text
    assert result.exit_code == 0


def test_allows_to_log_the_context(process_join_data, mocker, caplog):
    mocker.patch.object(process_join_data, "_connect_to_udm")
    stub_context = {"stub_name": "stub_value"}
    stub_context2 = {"stub_name2": "stub_value2"}
    mocker.patch.object(
        process_join_data,
        "load_context",
        side_effect=[stub_context, stub_context2],
    )

    with caplog.at_level(logging.DEBUG, logger="app"):
        result = runner.invoke(
            process_join_data.cli_app,
            [
                "example-data.yaml",
                "--log-context",
                "--template-context",
                "context.yaml",
                "--template-context",
                "context2.yaml",
            ],
        )

    assert "Merged context" in caplog.text
    assert result.exit_code == 0
