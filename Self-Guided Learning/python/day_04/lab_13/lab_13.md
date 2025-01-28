# Lab 13: [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)

In this lab, you will create a class hierarchy that demonstrates inheritance. You will create a base class called `Shape` and two subclasses called `Circle` and `Rectangle`. The `Shape` class will have a method called `area` that returns the area of the shape. The `Circle` class will have a method called `circumference` that returns the circumference of the circle. The `Rectangle` class will have a method called `perimeter` that returns the perimeter of the rectangle.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using a Google Colaboratory notebook or Jupyter notebook to run the code.

1. Create a new directory for this lab and navigate to it.
2. Create a new Python file called `shape.py`.
3. Define a class called `Shape` with a method called `area` that returns the area of the shape. The method should return `0.0`.

```python
class Shape:
    def area(self):
        print("Every shape has an area. But each shape has a different formula to calculate it.")
```

4. Define a class called `Circle` that inherits from the `Shape` class. The `Circle` class should have a method called `circumference` that returns the circumference of the circle. The method should return `0.0`.

```python
class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def circumference(self):
        return 3.14 * 2 * self.radius
    
    # NOTE: Overriding the area method from the Shape class
    def area(self):
        return 3.14 * self.radius ** 2
```

5. Define a class called `Rectangle` that inherits from the `Shape` class. The `Rectangle` class should have a method called `perimeter` that returns the perimeter of the rectangle. The method should return `0.0`.

```python
class Rectangle(Shape):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # NOTE: Overriding the area method from the Shape class
    def area(self):
        return self.width * self.height
```

6. Create an instance of the `Circle` class and call the `area` and `circumference` methods.

```python
circle = Circle()
print(circle.area())
print(circle.circumference())
```

7. Create an instance of the `Rectangle` class and call the `area` and `perimeter` methods.

```python
rectangle = Rectangle()
print(rectangle.area())
print(rectangle.perimeter())
```

### Optional Challenge

- Create a new subclass called `Square` that inherits from the `Rectangle` class. The `Square` class should have a method called `perimeter` that returns the perimeter of the square.
