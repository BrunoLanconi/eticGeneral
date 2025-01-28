# [Error Handling](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) and [Exceptions](https://docs.python.org/3/tutorial/errors.html#exceptions)

In Python, errors are represented by exceptions, which are objects that are raised when an error occurs. Exceptions can be caught and handled by the program, allowing it to recover from the error and continue executing. The `try` and `except` statements are used to catch and handle exceptions in Python.

### Example
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error: Division by zero.")
```

---

## Custom Exceptions

You can define your own exceptions by creating a new class that inherits from the `Exception` class. Custom exceptions can be raised and caught in the same way as built-in exceptions.

### Example
```python
class MyError(Exception):
    pass

try:
    raise MyError("An error occurred.")
except MyError as e:
    print(f"Error: {e}")
```

The `Exception` class has some built-in attributes and methods that can be used to customize the behavior of the exception. For example, you can define a custom error message by overriding the `__str__` method.

### Example
```python
class MyError(Exception):
    def __str__(self):
        return "An error occurred."
```

---

## Common Exceptions

Some common exceptions that you may encounter in Python include:

- `ZeroDivisionError`: Raised when division or modulo by zero is attempted.
- `ValueError`: Raised when a function receives an argument of the correct type but an inappropriate value.
- `TypeError`: Raised when an operation or function is applied to an object of inappropriate type.
- `KeyError`: Raised when a dictionary key is not found.
- `IndexError`: Raised when a sequence subscript is out of range.
