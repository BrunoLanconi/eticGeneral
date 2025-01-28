# Lab 09: Simple CLI

In this lab, you will create a simple command line interface (CLI) using the `click` module and manage the dependencies with Poetry.

## Prerequisites

- Python 3.x installed on your system
- Poetry installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using a container to isolate the project's dependencies.

1. Create a new directory for this lab and navigate to it.
2. Create a folder named `src` and add a new file named `commands.py` with the following content:

```python
# src/commands.py

import click

@click.command()
def hello():
    click.echo('Hello, World!')

if __name__ == '__main__':
    hello()
```

3. Initialize a new Poetry project:

```bash
poetry init
```

4. Add the `click` module as a dependency:

```bash
poetry add click
```

5. Run the script using Poetry:

```bash
poetry run python src/commands.py
```

6. Edit the `pyproject.toml` file to include the `src` folder as a package and the `hello` function as a script:

```toml
# pyproject.toml

[tool.poetry]
...
packages = [
    { include = "./src" }
]

[tool.poetry.scripts]
hello = "src.commands:hello"

...
```

8. Create a wheel package for the script:

```bash
poetry build
```

9. Install the package using the following command:

```bash
pip install dist/simple_cli-0.1.0-py3-none-any.whl
```

10. Run the script using the following command:

```bash
hello
```
