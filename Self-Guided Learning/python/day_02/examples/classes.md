## Defining a Simple Class
A class is defined using the `class` keyword, followed by the class name and a colon. The `__init__` method is a special method called constructor, which is executed when a new instance of the class is created.

### Example
```python
class Dog:
    """A simple class to represent a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over."""
        print(f"{self.name} rolled over!")


# Creating instances of the Dog class
my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

# Accessing attributes and calling methods
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
```

---

## Class with Methods
Classes can contain methods, which are functions that belong to the class.

### Example
```python
class Car:
    """A simple class to represent a car."""

    def __init__(self, make, model, year):
        """Initialize make, model, and year attributes."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# Creating an instance of the Car class
my_new_car = Car("audi", "a4", 2019)

# Accessing attributes and calling methods
print(my_new_car.get_descriptive_name())
```

---

## Inheritance
A class can inherit from one or more another class. The inherited class is called a child class, and the class it inherits from is called a parent class. In order to access the parent class's methods, use the `super()` function.

### Example
```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

# Creating an instance of the ElectricCar class
my_tesla = ElectricCar("tesla", "model s", 2019)

# Accessing attributes and calling methods
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

---

## Encapsulation
Encapsulation is the concept of restricting access to certain data and methods within a class. Use underscores to indicate that a method or attribute should be treated as private.

### Example
```python
class BankAccount:
    """A simple class to represent a bank account."""

    def __init__(self, owner, balance=0):
        """Initialize owner and balance attributes."""
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

# Creating an instance of the BankAccount class
my_account = BankAccount("John Doe", 1000)

# Accessing attributes and calling methods
print(my_account.owner)
my_account.deposit(500)
my_account.withdraw(200)
print(my_account.get_balance())
```

---

## Polymorphism
Polymorphism allows methods in different classes to have the same name but act differently.

### Example
```python
class Cat:
    """A simple class to represent a cat."""

    def __init__(self, name):
        """Initialize name attribute."""
        self.name = name

    def speak(self):
        """Simulate a cat speaking."""
        return f"{self.name} says Meow!"

class Dog:
    """A simple class to represent a dog."""

    def __init__(self, name):
        """Initialize name attribute."""
        self.name = name

    def speak(self):
        """Simulate a dog speaking."""
        return f"{self.name} says Woof!"

# Creating instances of Cat and Dog classes
cat = Cat("Whiskers")
dog = Dog("Fido")

# Using polymorphism to call the same method on different objects
animals = [cat, dog]
for animal in animals:
    print(animal.speak())
```

---

## [Class Abstraction](https://docs.python.org/3/library/abc.html)

Class abstraction is the process of hiding the implementation details of a class and only showing the essential features of the class. It allows you to define a blueprint for a class without providing the implementation details.

### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# NOTE: You cannot create an instance of an abstract class
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area

circle = Circle(5)
print(circle.area())  # Output: 78.5

rectangle = Rectangle(4, 3)
print(rectangle.area())  # Output: 12
```

You can also use abstract classes to define [abstract properties and class methods](https://docs.python.org/3/library/abc.html#abc.abstractmethod).

### Example
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @classmethod
    @abstractmethod
    def perimeter(cls):
        pass

class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @classmethod
    def perimeter(cls):
        return 3.14 * 2 * cls.radius

class Rectangle(Shape):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @classmethod
    def perimeter(cls):
        return 2 * (cls.width + cls.height)

circle = Circle(5)
print(circle.area)  # Output: 78.5
print(circle.perimeter())  # Output: 31.400000000000002
```

---

## @property Decorator

The `@property` decorator allows you to define a method that can be accessed like an attribute.

### Example
```python
class Circle:
    """A simple class to represent a circle."""

    def __init__(self, radius=1):
        """Initialize radius attribute."""
        self.radius = radius

    @property
    def area(self):
        """Calculate the area of the circle."""
        return 3.14 * self.radius ** 2

    @property
    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * 3.14 * self.radius

# Creating an instance of the Circle class
circle = Circle(5)

# Accessing the area and circumference attributes
print(circle.area)
print(circle.circumference)
```

---

## @classmethod and @staticmethod Decorators

The `@classmethod` and `@staticmethod` decorators allow you to define class methods and static methods, respectively. A class method takes the class itself as the first argument, while a static method does not take any special first argument.

### Example
```python
class Math:
    """A simple class to represent mathematical operations."""

    @classmethod
    def add(cls, a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

# Calling class and static methods
print(Math.add(5, 3))
print(Math.multiply(5, 3))
```
