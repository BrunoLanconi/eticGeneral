## Python Project

When organizing a Python project, it is important to follow a structure that makes the project maintainable and scalable. Here is an example of a typical Python project directory structure:

```text
my_project/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── module1.py
│   ├── module2.py
│   └── subpackage/
│       ├── __init__.py
│       ├── submodule1.py
│       └── submodule2.py
│
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
│
├── scripts/
│   └── some_script.py
│
├── data/
│   └── data_file.csv
│
├── .gitignore
├── pyproject.toml
└── README.md
```

### Project Directory (`my_project/`)

This is the root directory of the project. It contains all the necessary files and subdirectories.

### Package Directory (`my_project/src/`)

This directory contains the actual Python package. It usually has the same name as the project and includes an `__init__.py` file to mark it as a package.

```python
# my_project/src/__init__.py

# This file can be empty or contain package initialization code.
```

### Main Script (`src/main.py`)

This file typically contains the entry point of the program.

```python
# src/main.py

from src.module1 import some_function

if __name__ == "__main__":
    some_function()
```

### Modules (`src/module1.py` and `src/module2.py`)

These are individual Python files that contain reusable code.

```python
# src/module1.py

def some_function():
    print("This is a function in module1")
```

### Subpackage (`src/subpackage/`)

A subdirectory containing additional modules and an `__init__.py` file to make it a subpackage.

```python
# src/subpackage/__init__.py

# This file can be empty or contain subpackage initialization code.
```

```python
# src/subpackage/submodule1.py

def submodule_function():
    print("This is a function in submodule1")
```

### Tests Directory (`my_project/tests/`)

This directory contains test files, usually one for each module. Tests will be covered in more detail on Day 07.

```python
# my_project/tests/test_module1.py

import unittest
from src.module1 import some_function

class TestModule1(unittest.TestCase):
    def test_some_function(self):
        self.assertEqual(some_function(), "Expected Output")

if __name__ == "__main__":
    unittest.main()
```

### Scripts Directory (`my_project/scripts/`)

This directory can contain various utility scripts.

```python
# my_project/scripts/some_script.py

# This is a standalone script for some specific task.
```

### Data Directory (`my_project/data/`)

This directory is used to store data files such as CSV, JSON, etc.

### .gitignore File

This file specifies intentionally untracked files to ignore.

```text
# .gitignore

__pycache__/
*.pyc
*.pyo
.env
venv/
.idea/
.DS_Store
```

### README File (`README.md`)

This file provides information about the project.

```markdown
# README.md

# My Project

This is a sample Python project to demonstrate a typical project structure.
```

### pyproject.toml File

This file is used by the Poetry dependency management tool to manage project dependencies and settings.

```toml
# pyproject.toml

[tool.poetry]
name = "my_project"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]
readme = "README.md"
packages = [
    { include = "src" },
    { include = "src.subpackage" }
]

[tool.poetry.dependencies]
python = "^3.10"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
