## Defining a Simple Function
A function is defined using the `def` keyword, followed by the function name and parentheses which may include parameters.

### Example
```python
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World!
```

---

## Function with Parameters
Functions can take parameters to provide input data for processing.

### Example
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

---

## Function with Return Value
Functions can return values using the `return` keyword.

### Example
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

## Default Parameter Values
Functions can have default values for parameters, which are used if no argument is provided.

### Example
```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()        # Output: Hello, World!
greet("Alice") # Output: Hello, Alice!
```

---

## Keyword Arguments
Functions can be called using keyword arguments, where each argument is assigned by name.

### Example
```python
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Willie")               # Output: I have a dog named Willie.
describe_pet(pet_name="Harry", animal_type="cat") # Output: I have a cat named Harry.
```

---

## Arbitrary Number of Arguments
Functions can accept an arbitrary number of positional and keyword arguments using `*args` and `**kwargs`.

### Example
```python
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni", "mushrooms", "extra cheese")
# Output:
# Making a pizza with the following toppings:
# - pepperoni
# - mushrooms
# - extra cheese

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
# Output: {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}
```

---

## Lambda Functions
Lambda functions are small anonymous functions defined with the `lambda` keyword.

### Example
```python
# Lambda function to add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Lambda function to square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16
```

---

## Nested Functions
Functions can be defined inside other functions. These are called nested functions or inner functions.

### Example
```python
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the inner function!")
# Output: Hello from the inner function!
```

---

## Function Documentation
Use docstrings to provide documentation for your functions.

### Example
```python
def greet(name):
    """Greet the user by their name."""
    print(f"Hello, {name}!")

print(greet.__doc__)  # Output: Greet the user by their name.
```
