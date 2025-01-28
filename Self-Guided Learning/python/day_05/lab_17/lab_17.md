# Lab 17: Data Validation

Now that you have the `Calculator` class correctly typed, let's add some data validation to the class. We will use Pydantic to validate its data.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using the Google Colaboratory notebook or Jupyter notebook used to run the last lab code.

1. If you haven't already, remember to create a lab folder, initialize Poetry in the folder, and install Pydantic. For now on, for every lab, we will assume you have already done this step.
2. You `main.py` file should look like this:

```python
from pydantic import BaseModel

class AllModel(BaseModel):
    add: int
    subtract: int
    multiply: int
    divide: float
    power: int


class Calculator:
    def __init__(self, number: int) -> None:
        self.number = number

    def add(self, number: int) -> int:
        return self.number + number

    def subtract(self, number: int) -> int:
        return self.number - number

    def multiply(self, number: int) -> int:
        return self.number * number

    def divide(self, number: int) -> float:
        return self.number / number

    def power(self, number) -> int:
        return self.number ** number

    def all() -> AllModel:
        all_results = AllModel(
            add=self.add,
            subtract=self.subtract,
            multiply=self.multiply,
            divide=self.divide,
            power=self.power
        )

        return all_results
```

3. Just to illustrate, create a Pydantic model called `CalculatorModel` as shown below:

```python
from pydantic import BaseModel

class CalculatorModel(BaseModel):
    number: int

...
```

4. Create an instance of the `CalculatorModel` class and pass some number to it.

```python
...

calculator = CalculatorModel(number=5)
```

5. Print the `dict` representation of the `calculator` instance.

```python
...

print(calculator.dict())
```

6. Run the script and observe the output. Make some tests by changing the number to a string or a float.

```python
...

calculator = CalculatorModel(number="invalid")
```

7. Now let's change the `Calculator`. You may revert the changes you made to the `CalculatorModel` class. Change the `power` method to return a hardcoded value for now.

```python
...

    def power(self) -> float:  # Changed the return type to float and removed the number parameter
        return 2.3  # Hardcoded value for now
```

8. Run the script and observe the output. You should see a validation error.
9. Fix the error by changing `AllModel` to accept a `float` for the `power` key.

```python
...

class AllModel(BaseModel):
    add: int
    subtract: int
    multiply: int
    divide: float
    power: float  # Changed the type to float
```

10. Run the script and observe the output. You should see the `dict` representation of the `calculator` instance.
11. Reverse the changes you made to the `power` method and the `AllModel` class.

---

Your `main.py` file should look like this:

```python
from pydantic import BaseModel

class AllModel(BaseModel):
    add: int
    subtract: int
    multiply: int
    divide: float
    power: int


class Calculator:
    def __init__(self, number: int) -> None:
        self.number = number

    def add(self, number: int) -> int:
        return self.number + number

    def subtract(self, number: int) -> int:
        return self.number - number

    def multiply(self, number: int) -> int:
        return self.number * number

    def divide(self, number: int) -> float:
        return self.number / number

    def power(self, number: int) -> int:
        return self.number ** number

    def all() -> AllModel:
        all_results = AllModel(
            add=self.add,
            subtract=self.subtract,
            multiply=self.multiply,
            divide=self.divide,
            power=self.power
        )

        return all_results
```

### Optional Challenge

- Since we have our `Calculator` class correctly typed and validated, let's add some documentation to the class. Add a docstring to the `Calculator` class and its methods.