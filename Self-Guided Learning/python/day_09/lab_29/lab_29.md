# Lab 29: Error Handling

In this lab, you will learn how to handle errors in Python using the `try` and `except` statements - and how to get more information about the error that occurred.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `error_handling.py`.

```bash
$ touch error_handling.py
```

2. In the `error_handling.py` file, write a simple division operation that raises a `ZeroDivisionError`.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

This code snippet attempts to divide `1` by `0`, which raises a `ZeroDivisionError`. The `except` block catches the exception and prints the error message.

3. Add a `ValueError` to the `except` block to catch any other errors that may occur.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
```

This code snippet adds a `ValueError` to the `except` block to catch any other errors that may occur during the division operation.

4. Add a `finally` block to the `try` statement to execute cleanup code after the operation.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code")
```

The `finally` block will execute the cleanup code after the division operation, regardless of whether an error occurred.

5. Add a `raise` statement to the `except` block to re-raise the exception.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    raise
```

This code snippet re-raises the `ZeroDivisionError` after catching it in the `except` block.

6. Add a custom error message to the `raise` statement.

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    raise ValueError("Custom error message")
```

This code snippet re-raises the `ZeroDivisionError` as a `ValueError` with a custom error message.

7. Let's extract more information about the error that occurred. Add the following code snippet to the `except` block:

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e)}")
    print(f"Error message: {e.args[0]}")
```

This code snippet prints the type of the error and the error message using the `type` and `args` attributes of the exception object.
