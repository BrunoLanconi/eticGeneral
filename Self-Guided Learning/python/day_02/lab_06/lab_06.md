# Lab 06: Modules

Let's build a Python project that uses classes and modules. In this lab, you will create a Python project to interact with your terminal and environment variables using the `os` and `sys` modules.

## Prerequisites

- Python 3.x installed on your system
- Poetry installed on your system
- A text editor of your choice

## Instructions

As you made on the previous lab, create a new project using Poetry. Your project structure should look like this:

```text
lab_06/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── subpackage/
│       ├── __init__.py
│       └── submodule.py
│
├── pyproject.toml
└── README.md
```

## Script Challenge

Write a Python project that:

- Create a class named `Terminal` with the following methods:
  - `__init__`: Initializes the class with the current working directory.
  - `list_files`: Lists all files and directories in the current directory.
  - `create_directory`: Creates a new directory.
  - `rename_directory`: Renames a directory.
  - `remove_directory`: Removes a directory.
- Create a class named `Environment` with the following methods:
  - `__init__`: Initializes the class with the value of an environment variable.
  - `get_variable`: Gets the value of an environment variable.
  - `set_variable`: Sets the value of an environment variable.
- Create a function named `main` that:
  - Creates an instance of the `Terminal` class.
  - Lists all files and directories in the current directory.
  - Creates a new directory.
  - Renames the directory.
  - Removes the directory.
  - Creates an instance of the `Environment` class.
  - Gets the value of an environment variable.
  - Sets the value of an environment variable.

- **Attention**: Remember to `install` and `activate` the virtual environment before running the script.

```bash
poetry install
poetry shell
python main.py
```

- **Attention**: Remember to create a function and call it from `if __name__ == "__main__":`.

### Optional Challenge

- Modify the script to accept user input for the directory name and environment variable.

**Hint**: You may use [input](https://www.w3schools.com/python/ref_func_input.asp):

```python
fruit_name = input("What is the fruit name? ")
fruit_color = input("What is the fruit color? ")
```