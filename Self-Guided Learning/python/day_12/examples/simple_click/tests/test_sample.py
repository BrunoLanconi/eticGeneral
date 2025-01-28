"""
This file specifies tests cases sample.
"""

import shutil
import tempfile

import pytest

from src.cli.commands import simple_click
from src.services import cons


# This is how you access values passed through custom options
@pytest.fixture(scope="session", autouse=True)
def options(first_custom_option, second_custom_option) -> tuple:
    """
    Extracts values from custom options

    :param first_custom_option: a str representing custom --first-custom-option option value
    :param second_custom_option: a str representing custom --second-custom-option option value
    :return: a tuple of str representing custom options values
    """
    return first_custom_option, second_custom_option


@pytest.fixture
def monkey_patching(monkeypatch):
    """
    Use monkeypatch to mock attributes and create temporary files and directories.
    Use monkeypatch to clean environment after test running
    """
    # This is how you create a temporary directory
    temporary_dir = tempfile.mkdtemp(prefix="tmp", dir=".")

    # This is how you mock attributes
    monkeypatch.setattr(cons, "CONSTANT", "New constant sample")

    # Everything above yield is executed before tests
    yield  # Yield represents tests execution moment
    # Everything below yield is executed after tests

    shutil.rmtree(temporary_dir)


def test_sample(monkey_patching, isolated_cli_runner, options):
    first_custom_option = options[0]

    cli = simple_click  # CLI command to test
    args = ["-v", "first", "command-option", "-ok", first_custom_option]
    commands = "\n"

    result = isolated_cli_runner.invoke(cli=cli, args=args, input=commands)
    assert result.exit_code == 0
