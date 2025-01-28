"""This module contains classes that represent different shapes."""

import random


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


class Circle(Shape):
    """
    Represents a circle shape.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        circumference(): Calculates the circumference of the circle.
        area(): Calculates the area of the circle.
    """

    def __init__(self, radius=1):
        self.radius = radius

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 3.14 * 2 * self.radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14 * self.radius**2


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    # NOTE: Overriding the area method from the Shape class
    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height


class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        side (float): The length of the square's side.

    Methods:
        perimeter(): Calculates the perimeter of the square.
        area(): Calculates the area of the square.
    """

    def __init__(self, side=1):
        super().__init__(side, side)

    def perimeter(self):
        """
        Calculates the perimeter of the square.

        Returns:
            float: The perimeter of the square.
        """
        return 4 * self.width

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.width**2


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


def main():
    """
    This is the main function that demonstrates the usage of the Circle, Square and Rectangle classes.
    It creates instances of Circle, Square and Rectangle, calculates their area and circumference (or perimeter),
    creates a list of random shapes, sorts them by area in descending order, and prints the sorted list.
    """
    circle = Circle()
    print(circle.area())
    print(circle.circumference())

    rectangle = Rectangle()
    print(rectangle.area())
    print(rectangle.perimeter())

    shapes = create_random_shapes(5)
    shapes.sort(key=lambda x: x.area(), reverse=True)

    print("Shapes sorted by area:")
    for shape in shapes:
        print(shape)


if __name__ == "__main__":
    main()
