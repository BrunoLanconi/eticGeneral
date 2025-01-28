# Lab 03: Jupyter

With Python and Poetry installed, you can now create and run Jupyter notebooks on your local machine. Jupyter is a popular tool for interactive programming and data analysis, allowing you to write and execute code, create visualizations, and share your work with others.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Creating a Virtual Environment with Poetry

1. Install Poetry by following the instructions in the official documentation: [Poetry Installation](https://python-poetry.org/docs/#installation)

2. Navigate to the `jupyter` folder and run the following command to activate the virtual environment:

```bash
cd .../python/day_01/jupyter
poetry shell
```

3. Install the required dependencies specified in `pyproject.toml`:

```bash
poetry install
```

### More on Poetry

You can add new dependencies to your project based on the type of package you need. For example, to add a new package as a development dependency, run the following command:

```bash
poetry add --group dev <package-name>
```

This command will create a new section in `pyproject.toml` for development dependencies.

```toml
# pyproject.toml

...

[tool.poetry.group.dev.dependencies]
black = "^24.4.2"
ruff = "^0.5.1"
```

Then you may specify the group when installing the dependencies:

```bash
poetry install --only dev
```

Or you can specify the group that should NOT be installed:

```bash
poetry install --without dev
```

## Using Jupyter

1. Run the following command to start Jupyter within the virtual environment:

```bash
poetry run jupyter notebook
```

2. This will open Jupyter in your default web browser. You can now create, edit, and run notebooks.
