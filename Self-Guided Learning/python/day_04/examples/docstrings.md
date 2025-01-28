# [Docstrings](https://peps.python.org/pep-0257/)

Docstrings are used to document Python modules, classes, and functions. They are written as strings enclosed in triple quotes, and are placed at the beginning of the module, class, or function definition.

### Example
```python
def greet(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# NOTE: Special methods will be covered in Day 05
print(greet.__doc__)  # Output: Print a greeting message.
```

---

## Multi-Line Docstrings

Docstrings can span multiple lines to provide detailed documentation.

### Example
```python
def greet(name):
    """
    Print a greeting message.

    Args:
        name (str): The name of the person to greet.
    """
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# NOTE: Special methods will be covered in Day 05
print(greet.__doc__)
# Output:
# Print a greeting message.
#
# Args:
#     name (str): The name of the person to greet.
```

---

## Docstrings for Modules and Classes

Docstrings can also be used to document modules and classes.

### Example
```python
"""This module provides functions to greet people."""

class Greeter:
    """A class to generate
    greeting messages."""
    
    def greet(self, name):
        """Print a greeting message."""
        print(f"Hello, {name}!")

g = Greeter()
g.greet("Alice")  # Output: Hello, Alice!

# NOTE: Special methods will be covered in Day 05
print(Greeter.__doc__)  # Output: A class to generate greeting messages.
```

Accessing module docstrings:

### Example
```python
import module_name
print(module_name.__doc__)
```

---

## Function Annotations

Python allows you to add type hints to function parameters and return values using function annotations. These annotations are optional and do not enforce type checking.

### Example
```python
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

result = add(5, 3)
print(result)  # Output: 8

# NOTE: Annotations are stored in the __annotations__ attribute
print(add.__annotations__)  # Output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
```

Function annotations can be any expression, not just types:

### Example
```python
def greet(name: str = "World") -> None:
    """Print a greeting message."""
    print(f"Hello, {name}!")

greet()        # Output: Hello, World!
greet("Alice") # Output: Hello, Alice!

# NOTE: Annotations are stored in the __annotations__ attribute
print(greet.__annotations__)  # Output: {'name': <class 'str'>, 'return': <class 'NoneType'>}
```
