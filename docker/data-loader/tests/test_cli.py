import pytest
from typer.testing import CliRunner

runner = CliRunner()


def test_shows_help_information(process_join_data):
    result = runner.invoke(process_join_data.cli_app, ["--help"])
    assert result.exit_code == 0
