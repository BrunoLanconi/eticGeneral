# Lab 15: [Abstract Base Classes](https://docs.python.org/3/library/abc.html)

Now that we have our polymorphic basket of shapes, let's see how abstract base classes work in Python. In this lab, you will create an abstract base class called `Shape` that defines the `area` and `perimeter` methods. You will then create a `Circle` class that inherits from the `Shape` class and implements the `area` and `perimeter` methods.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using the Google Colaboratory notebook or Jupyter notebook used to run the last lab code.

1. Navigate to the directory created for the last lab.
2. In `shape.py`, import the `abc` module and define an abstract base class called `Shape` that defines the `area` and `perimeter` methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```

3. Define a class called `Circle` that inherits from the `Shape` class. The `Circle` class should implement the `area` and `perimeter` methods.

```python
class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
```

4. Create an instance of the `Circle` class and call the `area` and `perimeter` methods.

```python
circle = Circle()
print(circle.area())
print(circle.perimeter())
```

5. Run the script and observe the output.
6. Create a `main` function and call it if `__name__ == '__main__'`.

```python
def main():
    circle = Circle()
    print(circle.area())
    print(circle.perimeter())

if __name__ == "__main__":
    main()
```
