# Lab 14: Polymorphism

Now that we have our basket of shapes, let's see how polymorphism works in Python. In this lab, you will create a list of `Shape` objects that contains instances of the `Circle`, `Rectangle`, and `Square` classes. You will iterate over the list and call the `area` and `perimeter` methods for each object.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using the Google Colaboratory notebook or Jupyter notebook used to run the last lab code.

1. Navigate to the directory created for the last lab.
2. In `shape.py`, define a function called `create_random_shapes` that returns a list of randomly generated shapes. The function should take an integer `n` as a parameter and return a list of randomly generated shapes. The shapes should be instances of the `Circle`, `Rectangle`, and `Square` classes with random dimensions.

```python
def create_random_shapes(n: int):
    """
    Creates a list of randomly generated shapes.

    Parameters:
        n (int): The number of shapes to generate.

    Returns:
        list: A list of randomly generated shapes.
    """
    shapes = []

    for _ in range(n):
        shape = random.choice([Circle, Rectangle, Square])

        if isinstance(shape, Rectangle):
            shapes.append(shape(random.randint(1, 10), random.randint(1, 10)))
        else:
            shapes.append(shape(random.randint(1, 10)))
    return shapes
```

3. Since all the shapes have an `area` method, you can iterate over the list of shapes and call these methods for each object.
4. Lets create a `main` function and call it if `__name__ == '__main__'`.

```python
def main():
    """
    This is the main function that demonstrates the usage of the Circle, Square and Rectangle classes.
    It creates instances of Circle, Square and Rectangle, calculates their area and circumference (or perimeter),
    creates a list of random shapes, sorts them by area in descending order, and prints the sorted list.
    """
    shapes = create_random_shapes(5)
    shapes.sort(key=lambda x: x.area(), reverse=True)

    print("Shapes sorted by area:")
    for shape in shapes:
        print(shape.area())


if __name__ == "__main__":
    main()
```

5. As an introduction to special methods, let's add a `__str__` method to the `Shape` class that returns a stringified name of the shape and its area.

```python
class Shape:
    """
    Represents a generic shape.
    """

    def area(self):
        """
        Calculates the area of the shape.
        """
        print(
            "Every shape has an area. But each shape has a different formula to calculate it."
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__ }: {self.area()} area"
```

6. Now, when you print a shape object, you will see the name of the shape and its area.

```python
print(shapes[0])  # Circle: 3.14 area
```

### Optional Challenge

- Iterate over the list and call the `area` and `perimeter` methods for each object. 
- With a lambda function, sort the list of `Shape` objects by the area of each shape in ascending order.