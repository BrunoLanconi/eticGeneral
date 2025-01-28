# Lab 02: Installing and Using Poetry

With Python installed, now we need to separate our projects' dependencies from the system's dependencies. Poetry is a tool that helps manage Python dependencies and virtual environments. In this lab, you will learn how to install Poetry and use it to manage dependencies in your Python projects.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Step 1: [Installing Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Step 2: [Creating a New Project](https://python-poetry.org/docs/basic-usage/)

1. Create a new directory for your project:

```bash
mkdir my_project
cd my_project
```

2. Initialize a new Poetry project:

```bash
poetry init
```

This command will prompt you to enter some information about your project, such as its name, version, and dependencies. You can press Enter to accept the default values for now.

3. After completing the initialization, you will have a `pyproject.toml` file in your project directory. This file contains the project's metadata and dependencies.

```toml
[tool.poetry]
name = "lab-02"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [{include = "lab_02"}]

[tool.poetry.dependencies]
python = "^3.10"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## Step 3: [Managing Dependencies](https://python-poetry.org/docs/managing-dependencies/)

1. Search for the package you want to install on the [Python Package Index (PyPI)](https://pypi.org/).

2. Once you find the package, open your terminal and run the following command to add it as a dependency:

```bash
poetry add package_name
```

Replace `package_name` with the actual name of the package.

3. Poetry will automatically update your `pyproject.toml` file and create a `poetry.lock` file, which locks the versions of your dependencies.

4. To install the dependencies, run the following command:

```bash
poetry install
```

Poetry will create a virtual environment and install the dependencies inside it.

## Step 4: [Running Scripts](https://python-poetry.org/docs/cli/#run)

```bash
poetry run python my_script.py
```

Replace `my_script.py` with the name of your script. Try `python/day_01/lab_02/main.py`.
