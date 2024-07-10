import importlib.util
import os
import os.path

import pytest
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture
def process_join_data():
    """Provide "process-join-data.py" as a module."""
    module_name = "process_join_data"
    module_path = "./bin/process-join-data.py"
    spec = importlib.util.spec_from_file_location(
        module_name,
        os.path.join(module_path),
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_shows_help_information(process_join_data):
    result = runner.invoke(process_join_data.cli_app, ["--help"])
    assert result.exit_code == 0
