# Lab 28: Custom Exception

In this lab, you will learn how to create a custom exception in Python.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `custom_exception.py`.

```bash
$ touch custom_exception.py
```

2. In the `custom_exception.py` file, create a custom exception class called `CustomException`.

```python
class CustomException(Exception):
    pass
```

This is the simplest form of a custom exception class in Python. You can add custom attributes and methods to the class as needed.

3. Create an instance of the `CustomException` class and raise it.

```python
try:
    raise CustomException("This is a custom exception")
except CustomException as e:
    print(e)
```

This code snippet creates an instance of the `CustomException` class with a custom message and raises it. The `except` block catches the exception and prints the custom message.

4. Add custom attributes and methods to the `CustomException` class as needed.

```python
class CustomException(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"{self.code}: {self.args[0]}"
```

In this example, we added a custom `code` attribute to the `CustomException` class and modified the `__init__` and `__str__` methods to include the `code` attribute in the exception message.

5. Create an instance of the `CustomException` class with custom attributes and raise it.

```python
try:
    raise CustomException("This is a custom exception", 500)
except CustomException as e:
    print(e)
```

This code snippet creates an instance of the `CustomException` class with a custom message and code and raises it. The `except` block catches the exception and prints the custom message and code.
