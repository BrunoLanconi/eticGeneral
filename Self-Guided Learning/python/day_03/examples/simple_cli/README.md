# Simple CLI

The `click` module is a Python package for creating command line interfaces. It is a powerful tool that can be used to create complex command line interfaces with minimal effort. In this example, we will create a simple command line interface using the `click` module.

## Commands

```bash
bash                           Run a bash shell in the Docker container
build                          Build the Docker image
help                           Show help
```

---

## [Commands and Groups](https://click.palletsprojects.com/en/8.1.x/commands/#commands-and-groups)

At the core of the `click` module is the `click.command` decorator, which is used to define a command line interface. The `click.command` decorator takes a number of arguments that can be used to customize the behavior of the command.

### Example
```python
import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")

@cli.command()  # @cli, not @click!
def sync():
    click.echo('Syncing')
```

```bash
<command-name> --debug sync
```

---

### Creating subcommands

The `click.group` decorator can be used to create a group of commands. Each command within the group is defined using the `@cli.command()` decorator.

### Example
```python

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo('Hello!')

@cli.command()
def goodbye():
    click.echo('Goodbye!')
```

```bash
<command-name> hello
<command-name> goodbye
```

___

## [Options](https://click.palletsprojects.com/en/8.1.x/options/)

The `click.option` decorator is used to define options for a command. Options can be used to customize the behavior of a command or to provide additional information to the user.

### Example
```python
@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    click.echo(f'Hello, {name}!')
```

```bash
<command-name> --name John
```

---

## [Arguments](https://click.palletsprojects.com/en/8.1.x/arguments/)

The `click.argument` decorator is used to define arguments for a command. Arguments are positional parameters that are passed to a command when it is invoked.

### Example
```python
@click.command()
@click.argument('name')
def hello(name):
    click.echo(f'Hello, {name}!')
```

```bash
<command-name> John
```

---

## Click with Poetry

You can use Poetry to create a wheel file for your CLI application. This will allow you to distribute your application as a standalone package that can be installed using `pip`.

### Example
```bash
poetry build
```

This will create a `dist` directory containing a wheel file for your application. You can then install the application using `pip`.

```bash
pip install dist/<package-name>-<version>-py3-none-any.whl
```

Imagine the following project structure:

```bash
.
├── README.md
├── poetry.lock
├── pyproject.toml
└── src
    └── commands.py
```

Where `src/commands.py` contains your CLI commands:

```python
import click

@click.command()
def hello():
    click.echo('Hello, world!')

if __name__ == '__main__':
    hello()
```

Then you should add the following to your `pyproject.toml` file:

```toml
[tool.poetry]
...
packages = [
    { include = "./src" }
]

[tool.poetry.scripts]
hello = "src.commands:hello"

...
```

This configuration will create a CLI command called `hello` that will run the `hello` function in `src/commands.py` when installing the wheel file created by `poetry build` command.