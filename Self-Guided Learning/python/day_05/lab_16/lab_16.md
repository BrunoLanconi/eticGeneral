# Lab 16: Type Hinting

Below you will find some Python functions within a class. Your task is to add type hints to the functions and variables. For example, the `add` function should have a type hint of `int` for the `number` parameter and the return type. The `number` variable should have a type hint of `int`.

### Example
```python
class Calculator:
    def __init__(self, number: int):
        self.number = number
    ...
```

For `all()` function, since it return a `dict`, create a Pydantic model to return the dictionary with the correct types.

### Example
```python
from pydantic import BaseModel

class SampleModel(BaseModel):
    a: str
    b: int

class SampleClass:
    def sample_function(self) -> AllModel:
        return {
            'a': 'Hello',
            'b': 1
        }
```

## Prerequisites

- A text editor of your choice

## Exercise

```python
class Calculator:
    def __init__(self, number):
        self.number = number

    def add(self, number):
        return self.number + number

    def subtract(self, number):
        return self.number - number

    def multiply(self, number):
        return self.number * number

    def divide(self, number):
        return self.number / number

    def power(self, number):
        return self.number ** number

    def all():
        return {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'power': self.power
        }
```