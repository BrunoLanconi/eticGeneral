"""
This file specifies configurations for PyTest related methods.
"""

import pytest


# This is how you add custom options to pytest command
# E.g. pytest --custom-option
def pytest_addoption(parser):
    """
    Add custom options to pytest
    """
    parser.addoption(
        "--first-custom-option",
        default="First custom option value",
        help="A str representing the first custom option value",
    )
    parser.addoption(
        "--second-custom-option",
        default="Second custom option value",
        help="A str representing the second custom option value",
    )


@pytest.fixture(scope="session", autouse=True)
def first_custom_option(request):
    """
    custom --first-custom-option option
    """
    return request.config.getoption(name="--first-custom-option")


@pytest.fixture(scope="session", autouse=True)
def second_custom_option(request):
    """
    custom --second-custom-option option
    """
    return request.config.getoption(name="--second-custom-option")
