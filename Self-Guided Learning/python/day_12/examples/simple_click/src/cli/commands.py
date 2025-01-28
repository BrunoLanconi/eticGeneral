"""
This file specifies commands used by CLI and its behaviors.
"""

import logging

import click

from src.services.log import logger
from src.services.main import main_service


@click.group()
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    flag_value="verbose",
    help="Prints all verbosity messages.",
)
def simple_click(verbosity: str):
    """
    :param verbosity: a str representing verbosity level
    """
    is_verbose = verbosity == "verbose"

    if is_verbose:
        logger.setLevel(level=logging.DEBUG)


# Use 'name' argument to overwrite the Click default command naming method
# E.g. This command call would be 'first-command-group' but since name argument is defined it is 'first'
# click.group decorators are responsible for grouping command chains
@click.group(name="first")
@click.pass_context  # Use click.pass_context to pass contexts between groups and commands
def first_command_group(ctx: click.Context):
    """
    Use docstrings to define the group or command help message

    :param ctx: a Context object representing the possibility to pass contexts through commands
    """
    # When using click.pass_context decorator, use ctx.ensure_object to ensure
    # the context passing needed object exists and is the expected type.
    # There is no need to call ctx.ensure_object on every command chain
    ctx.ensure_object(dict)

    # This is how you pass context variables
    ctx.obj["context_variable"] = "context_value"


@click.command
@click.pass_context
# This is how you define a command argument.
# The arguments stay at the end of the command call and cannot be blank.
# E.g. simple_click first command-argument ARGUMENT
@click.argument("argument")
def command_argument(ctx: click.Context, argument: str):
    """
    Logs context variable on DEBUG level and argument on INFO level

    :param ctx: a Context object representing the possibility to pass contexts through commands
    :param argument: use docstrings to define argument help message
    """
    logger.debug(f'Context variable: {ctx.obj["context_variable"]}')
    logger.info(f"Argument: {argument}")


@click.command
# This is how you define a command option.
# Every option value proceed its own key and can be omitted if 'required' argument is False.
# E.g. simple_click first command-option --option-key option_value
# E.g.² simple_click first command-option -ok option_value
# click.option will consider the last argument as the programmatically variable name
# and the others as key name variation
@click.option(
    "-ok",
    "--option-key",
    "option_value",
    required=False,
    help="Use click.option 'help' argument to define option help message.",
)
def command_option(option_value: str):
    """
    Logs option value on INFO level and runs the main service, which logs the welcome message

    :param option_value: a str representing the option value
    """
    logger.info(option_value)
    main_service()


# Use add_command to create a command chain.
# E.g.
# simple_click
#   first_command_group
#       command_argument
#       command_option
first_command_group.add_command(command_argument)
first_command_group.add_command(command_option)
simple_click.add_command(first_command_group)

if __name__ == "__main__":
    simple_click()
