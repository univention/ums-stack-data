# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024-2025 Univention GmbH

import logging
from unittest.mock import patch

from typer.testing import CliRunner

from univention.data_loader import cli

runner = CliRunner()


DEFAULT_ENV = {
    "UDM_API_URL": "stub_url",
    "UDM_API_USER": "stub_user",
    "UDM_API_PASSWORD_FILE": "stub_password",
}


stub_context = {"stub_name": "stub_value"}
stub_context2 = {"stub_name2": "stub_value2"}

udm_api_url = "stub_udm_api_url"
udm_api_user = "stub_udm_api_user"
udm_api_password = "stub_udm_api_password"
udm_api_password_file = "stub_udm_api_password_file"


def test_shows_help_information():
    result = runner.invoke(cli.cli_app, ["--help"])
    assert result.exit_code == 0


@patch("univention.data_loader.cli.process_template.run")
@patch("univention.data_loader.cli._connect_to_udm")
class TestCliArguments:
    def test_accepts_filename_as_argument(self, mock_udm, mock_run):
        result = runner.invoke(
            cli.cli_app,
            ["examples/example-data.yaml"],
            env=DEFAULT_ENV,
        )

        mock_run.assert_called_once()
        assert mock_run.call_args[0][1] == "examples/example-data.yaml"
        assert result.exit_code == 0

    def test_accepts_template_extension_as_option(self, mock_udm, mock_run):
        result = runner.invoke(
            cli.cli_app,
            ["examples/example-data.yaml", "--template-extension", ".j2"],
            env=DEFAULT_ENV,
        )

        assert mock_run.call_args.kwargs["template_extension"] == ".j2"
        assert result.exit_code == 0

    @patch("univention.data_loader.cli.load_context", return_value=stub_context)
    def test_accepts_template_context_as_option(
        self,
        mock_load_context,
        mock_udm,
        mock_run,
    ):
        result = runner.invoke(
            cli.cli_app,
            ["examples/example-data.yaml", "--template-context", "context.yaml"],
            env=DEFAULT_ENV,
        )

        mock_load_context.assert_called_once_with("context.yaml")
        assert mock_run.call_args.kwargs["template_context"] == stub_context
        assert result.exit_code == 0

    @patch(
        "univention.data_loader.cli.load_context",
        side_effect=[stub_context, stub_context2],
    )
    def test_accepts_multiple_template_context_options(
        self,
        mock_load_context,
        mock_udm,
        mock_run,
    ):
        result = runner.invoke(
            cli.cli_app,
            [
                "examples/example-data.yaml",
                "--template-context",
                "context.yaml",
                "--template-context",
                "context2.yaml",
            ],
            env=DEFAULT_ENV,
        )

        expected_context = stub_context | stub_context2
        assert mock_run.call_args.kwargs["template_context"] == expected_context
        assert result.exit_code == 0


@patch("univention.data_loader.cli._connect_to_udm")
@patch(
    "univention.data_loader.cli.load_context",
    side_effect=[stub_context, stub_context2],
)
class TestLogging:
    def test_does_not_log_context_by_default(self, mock_load_context, mock_udm, caplog):
        with caplog.at_level(logging.DEBUG, logger="app"):
            result = runner.invoke(
                cli.cli_app,
                [
                    "examples/example-data.yaml",
                    "--template-context",
                    "context.yaml",
                    "--template-context",
                    "context2.yaml",
                ],
                env=DEFAULT_ENV,
            )

        assert "Merged context" not in caplog.text
        assert result.exit_code == 0

    def test_allows_to_log_the_context(self, mock_load_context, mock_udm, caplog):
        with caplog.at_level(logging.DEBUG, logger="app"):
            result = runner.invoke(
                cli.cli_app,
                [
                    "examples/example-data.yaml",
                    "--log-context",
                    "--template-context",
                    "context.yaml",
                    "--template-context",
                    "context2.yaml",
                ],
                env=DEFAULT_ENV,
            )

        assert "Merged context" in caplog.text
        assert result.exit_code == 0


@patch("univention.data_loader.cli._connect_to_udm")
@patch("univention.data_loader.cli.load_context", return_value=stub_context)
class TestContextRendering:
    def test_does_not_log_the_rendered_template_by_default(
        self,
        mock_load_context,
        mock_udm,
        caplog,
    ):
        with caplog.at_level(logging.DEBUG, logger="app"):
            result = runner.invoke(
                cli.cli_app,
                [
                    "examples/example-data.yaml",
                    "--template-context",
                    "context.yaml",
                ],
                env=DEFAULT_ENV,
            )

        assert "Rendered template" not in caplog.text
        assert result.exit_code == 0

    def test_allows_to_log_the_rendered_template(
        self,
        mock_load_context,
        mock_udm,
        caplog,
    ):
        with caplog.at_level(logging.DEBUG, logger="app"):
            result = runner.invoke(
                cli.cli_app,
                [
                    "examples/example-data.yaml",
                    "--log-template",
                    "--template-context",
                    "context.yaml",
                ],
                env=DEFAULT_ENV,
            )

        assert "Rendered template" in caplog.text
        assert result.exit_code == 0


@patch("univention.data_loader.cli.UDM")
@patch("univention.data_loader.cli.read_from_file", return_value=udm_api_password)
@patch("univention.data_loader.cli.process_template.run")
class TestUDMConfig:
    def test_allows_to_configure_the_udm_connection_via_cli(
        self,
        mock_run,
        mock_read_from_file,
        mock_udm_client,
    ):
        result = runner.invoke(
            cli.cli_app,
            [
                "examples/example-data.yaml",
                "--udm-api-url",
                udm_api_url,
                "--udm-api-user",
                udm_api_user,
                "--udm-api-password-file",
                udm_api_password_file,
            ],
            catch_exceptions=False,
        )

        mock_read_from_file.assert_called_once_with(udm_api_password_file)
        mock_udm_client.http.assert_called_once_with(
            udm_api_url,
            udm_api_user,
            udm_api_password,
        )
        assert result.exit_code == 0

    def test_configures_udm_connection_based_on_environment_variables(
        self,
        mock_run,
        mock_read_from_file,
        mock_udm_client,
    ):
        env = {
            "UDM_API_URL": udm_api_url,
            "UDM_API_USER": udm_api_user,
            "UDM_API_PASSWORD_FILE": udm_api_password_file,
        }

        result = runner.invoke(
            cli.cli_app,
            ["examples/example-data.yaml"],
            catch_exceptions=False,
            env=env,
        )

        mock_read_from_file.assert_called_once_with(udm_api_password_file)
        mock_udm_client.http.assert_called_once_with(
            udm_api_url,
            udm_api_user,
            udm_api_password,
        )
        assert result.exit_code == 0
