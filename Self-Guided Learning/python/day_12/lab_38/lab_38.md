# Lab 38: Build with Poetry

Based on the previous lab, you will build the calculator application using Poetry.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new folder `calculator` and place `calculator.py` inside it.
2. In `calculator` folder initialize a new Poetry project.

```shell
poetry init
```

3. Fill in the project details as needed.
4. Add Click as a dependency.

```shell
poetry add click
```

5. Add the `tool.poetry.scripts` section to the `pyproject.toml` file.

```toml
# pyproject.toml
...

[tool.poetry.scripts]
calculator = "calculator:cli"

...
```

6. Install the application in the virtual environment.

```shell
poetry install
```

**Note**: Poetry may argue that `README.md` is missing. You can create an empty file to satisfy the requirement.

7. Run the application.

```shell
poetry run calculator
```

8. Test the application by adding two numbers.

```shell
poetry run calculator add 2 3
```

9. Now you can build the application.

```shell
poetry build
```

10. Check the `dist` folder for the built and gather the file name ending with `.whl`.
11. Install the built package.

```shell
pip install dist/<package-name>.whl
```

12. Run the installed package.

```shell
calculator add 5 6
```

**Note**: Remember that `pip` will install the package on the current environment. If the virtual environment is active, the package will be installed there. If you want to install the package globally, deactivate the virtual environment before running the `pip install` command.

13. To remove the installed package, run the following command.

```shell
pip uninstall <package-name>
```