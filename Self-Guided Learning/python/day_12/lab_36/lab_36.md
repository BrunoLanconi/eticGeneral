# Lab 36: Create Commands

In this lab, you will create a Click command line application that behaves like a simple calculator. The application should have the following commands:

- `add`: Add two numbers
- `subtract`: Subtract two numbers
- `multiply`: Multiply two numbers
- `divide`: Divide two numbers

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `calculator.py`.	
2. In `calculator.py`, create a `group` object called `cli` using the `click.group()` decorator.

```python
import click

@click.group()
def cli():
    pass
```

3. Create a command called `add` that takes two arguments, `a` and `b`, and adds them together. Use the `click.argument()` decorator to define the arguments.

```python
...
@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def add(a, b):
    click.echo(a + b)
```

4. Create commands for `subtract`, `multiply`, and `divide` that perform the corresponding operations on two numbers.

```python
...
@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def subtract(a, b):
    click.echo(a - b)

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def multiply(a, b):
    click.echo(a * b)

@cli.command()
@click.argument('a', type=int)
@click.argument('b', type=int)
def divide(a, b):
    click.echo(a / b)
```

5. Add the following code to the end of the file to run the `cli` group.

```python
...
if __name__ == '__main__':
    cli()
```

6. Run the `calculator.py` file from the command line and test the `add`, `subtract`, `multiply`, and `divide` commands with different numbers.

```shell
$ python calculator.py add 5 3
8
$ python calculator.py subtract 10 5
5
$ python calculator.py multiply 4 6
24
$ python calculator.py divide 10 2
5.0
```

### Optional Challenge

- Implement additional commands for calculating the square root, power, and modulus of a number.
- Add support for floating-point numbers in the calculator commands.
- Display an error message if the user tries to divide by zero.
- Document the commands using the `@click.command()` decorator and provide help text for each command.