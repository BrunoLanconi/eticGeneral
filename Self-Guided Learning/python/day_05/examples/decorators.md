## [Decorators](https://wiki.python.org/moin/PythonDecorators)

Python decorators are a way to modify or extend the behavior of functions or methods. They are a form of metaprogramming and can be used to add functionality to existing functions or methods without changing their code. Decorators are a powerful tool in Python and are commonly used in web frameworks like Flask and Django to add functionality to views and routes.

### Example
```python
def uppercase(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: HELLO, ALICE!
```

---

## Arguments

Decorators can take arguments to customize their behavior. This is achieved by defining a decorator function that returns a decorator. The outer decorator function takes the arguments and returns the inner decorator function, which in turn takes the function to be decorated.

### Example
```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(n)]
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']
```

---

## Class Decorators

Decorators can also be applied to classes. In this case, the decorator function takes the class as an argument and returns a new class that extends the original class.

### Example
```python
def add_method(cls):
    def wrapper(self):
        return "This is a new method."
    cls.new_method = wrapper
    return cls

@add_method
class MyClass:
    def existing_method(self):
        return "This is an existing method."

obj = MyClass()

print(obj.existing_method())  # Output: This is an existing method.
print(obj.new_method())  # Output: This is a new method.
```

---

## Decorator Classes

Decorators can also be implemented as classes. The class must implement the `__call__` method, which allows instances of the class to be called as functions.

### Example
```python
class Uppercase:
    def __init__(self, func):
        self.func = func

    def __call__(self, text):
        result = self.func(text)
        return result.upper()

@Uppercase
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: HELLO, ALICE!
```

---

## Built-in Decorators - @staticmethod

The `@staticmethod` decorator is used to define a static method in a class. Static methods do not have access to the instance or class attributes and are mainly used for utility functions that do not depend on the state of the object.

### Example
```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))  # Output: 5
```

---

## Built-in Decorators - @classmethod

The `@classmethod` decorator is used to define a class method in a class. Class methods take a `cls` parameter that points to the class itself and can be used to access class variables and methods.

### Example
```python
class Math:
    value = 10

    @classmethod
    def get_value(cls):
        return cls.value

print(Math.get_value())  # Output: 10
```

---

## Built-in Decorators - @property

The `@property` decorator is used to define a property in a class. Properties allow you to define getter, setter, and deleter methods for an attribute, making it easier to work with class attributes.

### Example
```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)

print(circle.area)  # Output: 78.5
```

---

## Chaining Decorators

Decorators can be chained by applying multiple decorators to a single function or method. The order of decorators is important, as they are applied from the innermost to the outermost decorator. The sample below first applies the `repeat` decorator and then the `uppercase` decorator.

### Example
```python
def uppercase(func):
    def wrapper(text):
        result = func(text)
        return result.upper()
    return wrapper

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(n)]
            return results
        return wrapper
    return decorator

@repeat(3)
@uppercase
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: ['HELLO, ALICE!', 'HELLO, ALICE!', 'HELLO, ALICE!']
```
