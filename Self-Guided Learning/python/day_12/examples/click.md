# [Click](https://click.palletsprojects.com/en/8.1.x/)

Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It's the "Command Line Interface Creation Kit". It's highly configurable but comes with sensible defaults out of the box.

### Example
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```

Then you can run the program like this:

### Example
```shell
$ python hello.py --count=3
Your name: John
Hello John!
Hello John!
Hello John!
```

---

## [Commands and Groups](https://click.palletsprojects.com/en/8.1.x/commands/)

Click provides a way to define commands and groups of commands. A group is a collection of commands that share a common context. This is useful when you have a set of commands that are related to each other in some way.

### Example
```python
import click

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
```

Then you can run the program like this:

### Example
```shell
$ python hello.py initdb
Initialized the database
$ python hello.py dropdb
Dropped the database
```

---

## [Options and Arguments](https://click.palletsprojects.com/en/8.1.x/options/)

Click provides a way to define options and arguments for your commands. Options are flags that can be passed to your command, while arguments are positional arguments that are passed to your command.

### Example
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.argument('name')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```

Then you can run the program like this:

### Example
```shell
$ python hello.py --count=3 Alice
Hello Alice!
Hello Alice!
Hello Alice!
```

---

# [Contexts](https://click.palletsprojects.com/en/8.1.x/contexts/)

Click provides a way to define contexts for your commands. A context is a dictionary that contains information about the current state of your program. This is useful when you need to pass information between commands.

### Example
```python
import click

@click.command()
@click.pass_context
def cli(ctx):
    ctx.obj = {'foo': 42}

@cli.command()
@click.pass_context
def subcommand(ctx):
    click.echo(ctx.obj['foo'])

if __name__ == '__main__':
    cli()
```

Then you can run the program like this:

### Example
```shell
$ python hello.py subcommand
42
```

---

# [Click and Poetry](https://click.palletsprojects.com/en/8.1.x/setuptools/)

Calling Click commands using `python <script>.py` is not the best way to run your commands. You can use Poetry to create a package and install it using `pip`. This way, you can call your commands using the package name.

Usually, we start with a simple command like this:

### Example
```python
# src/cli/commands.py
import click

@click.command()
@click.argument('arg')
def simple_click(arg):
    click.echo(f'Argument: {arg}')
```

Then you can run the program like this:

### Example
```shell
$ python src/cli/commands.py ARGUMENT
Argument: ARGUMENT
```

Now that we have our `simple_click` command, we need to specify the command reference in the `pyproject.toml` file.

### Example
```toml
# pyproject.toml
...

[tool.poetry.scripts]
simple_click = "src.cli.commands:simple_click"

...
```

Then we may build the package and install it using Poetry.

### Example
```shell
$ poetry build
$ pip install dist/simple_click-0.1.0.tar
```

Now you can run the command like this:

### Example
```shell
$ simple_click ARGUMENT
Argument: ARGUMENT
```

---

# [Testing](https://click.palletsprojects.com/en/8.1.x/testing/)

Click provides a way to test your commands using the `CliRunner` class. This class allows you to run your commands in a test environment and check the output. Imagine you have a simple command like this:

### Example
```python
# src/cli/commands.py
import click

@click.command()
@click.argument('arg')
def simple_click(arg):
    click.echo(f'Argument: {arg}')
```

We can create a test for this command using the `CliRunner` class.

### Example
```python
# tests/test_commands.py
from click.testing import CliRunner
from src.cli.commands import simple_click

def test_simple_click():
    runner = CliRunner()
    result = runner.invoke(simple_click, ['ARGUMENT'])

    assert result.exit_code == 0
    assert result.output == 'Argument: ARGUMENT\n'
```

On `python/day_12/examples/simple_click` you can find a complete example of a Click command with tests. There is also a `Makefile` with commands to create a new environment, run tests, and create documentation. For this project, we used `pdoc` to create the documentation and `pytest` to run the tests - just to introduce you to these alternative tools. Enjoy!
