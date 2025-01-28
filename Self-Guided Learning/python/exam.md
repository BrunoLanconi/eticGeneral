# Exam

Below you will find a list of questions that you need to answer. The questions are grouped by day as they were presented in the course. 

- Day 01: Python Intro
- Day 02: Python Fundamentals
- Day 03: VEnvs, Docker and Libraries
- Day 04: Python Intermediate 01
- Day 05: Python Intermediate 02
- Day 06: Models, Comprehension and Databases
- Day 07: APIs with FastAPI and Django Rest Framework 
- Day 08: Web with Django
- Day 09: Debug, Logging, Tests and Error Handling
- Day 10: Files and Requests
- Day 11: Pandas and Plotting
- Day 12: CLI with Click
- Day 13: Python Project

Each day has at least 02 questions of multiple choice, multiple selection or true or false. Each question has a weight that represents the importance of the question. The total sum of the weights is 100. The exam is open book, meaning you can use any resources you want to answer the questions. You can use the internet, your notes, the course materials, etc. You can also use the Python interpreter to test your code, but try to use none or as little as possible in order to challenge yourself. The exam is individual, meaning you should not discuss the questions with your colleagues. You have 2 hours to complete the exam. Good luck!

---

## Day 01: Python Intro

### Question 1 (weight: 1; total: 1)

What is the output of the following code?

```python
a = 10
b = 20
c = a + b

print(c)
```

a) 10
b) 20
c) 30
d) 1020

### Question 2 (weight: 1; total: 2)

What is the command to enter the interactive Python interpreter?

a) `python`
b) `python3`
c) `python3.10`
d) All options are correct

### Question 3 (weight: 1; total: 3)

How do you run a Python script from the command line. The current directory is `~/Documents`, the script is located in `~/Documents/my-script` and is called `script.py`.

a) `python script.py`
b) `python my-script/script.py`
c) `python ~/Documents/my-script`
d) `python my-script`

### Question 4 (weight: 3; total: 6)

Poetry, venv, pipenv and conda are all tools to:

a) Create virtual environments and manage dependencies
b) Control the Python interpreter and the Python standard library
c) Clear the Python cache and temporary files
d) Share Python code with other developers and evaluate code quality

### Question 5 (weight: 5; total: 11)

What is the output of the following code?

```python
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

for key, value in my_dict.items():
    if value % 2 == 0:
        print(f'{key}: {value}')

    else:
        print(f'{key}: {value * 2}')
```

a)
```
a: 1
b: 2
c: 3
```
b) 
```
a: 1
b: 4
c: 3
```
c) 
```
a: 1
b: 2
c: 6
```
d) 
```
a: 2
b: 2
c: 6
```

---

## Day 02: Python Fundamentals

### Question 6 (weight: 3; total: 14)

What is the output of the following code?

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'MyClass({self.value})'

obj = MyClass(10)
print(obj)
```

a) `MyClass(10)`
b) `MyClass`
c) `10`
d) `MyClass object`

### Question 7 (weight: 5; total: 19)

What is the output of the following code?

```python
class Geometry:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Triangle(Geometry):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        a, b, c = self.sides
        s = sum(self.sides) / 2

        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

triangle = Triangle([3, 4, 5])
print(triangle.create_perimeter())
```

a) `12`
b) A TypeError is raised
c) An AttributeError is raised
d) `6.0`

---

## Day 03: VEnvs, Docker and Libraries

### Question 8 (weight: 1; total: 20)

A Python virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. Pandas and Django are examples of tools for creating virtual environments.

a) True
b) False

### Question 9 (weight: 3; total: 23)

Select the options that are correct:

[] Click is a Python library for creating command-line interfaces
[] FastAPI is a Python library for creating parallel applications
[] Django is a Python library for creating web applications
[] Flask is a Python library for handling Docker containers

---

## Day 04: Python Intermediate 01

### Question 10 (weight: 1; total: 24)

The Poetry command to add a package on `development` group is:

a) `poetry add --group development <package>`
b) `poetry add <package>`
c) `poetry add --dev <package>`
d) `poetry add --optional <package>`

### Question 11 (weight: 1; total: 25)

And the one to install only the packages from the `production` group is:

a) `poetry install`
b) `poetry install --production`
c) `poetry install --no-dev`
d) `poetry install --only production`

### Question 12 (weight: 3; total: 28)

What is the output of the following code?

```python
def my_func(*args, **kwargs):
    for arg in args:
        print(arg)
    
    for key, value in kwargs.items():
        print(f'{key}: {value}')

my_func(1, 2, 3, a=10, b=20)
```

a)
```
a: 10
b: 20
1
2
3
```
b)
```
1
2
3
a: 10
b: 20
```
c)
```
1
2
3
```
d)
```
a: 10
b: 20
```

### Question 13 (weight: 5; total: 33)

What is the output of the following code?

```python
class BaseClass:
    def __init__(self, value: int):
        self.value = value

    def multiply(self, factor: int):
        return self.value * factor

class DerivedClass(BaseClass):
    def __init__(self, value: int):
        super().__init__(value)

    def divide(self, factor: int):
        return self.value / factor
    
class FinalClass(DerivedClass):
    def __init__(self, value: int):
        super().__init__(value)

    def divide(self, factor: int):
        result = super().divide(factor)

        return result / factor

classes = [BaseClass(10), DerivedClass(10), FinalClass(10)]

print(classes[1].divide(2))
print(classes[2].divide(2))

for _ in classes:
    print(_.multiply(2))
```

a)
```
5.0
5.0
20
20
20
```
b)
```
10.0
5.0
10
10
10
```
c)
```
5.0
2.5
20
20
20
```
d)
```
5.0
2.5
10
10
10
```

---

## Day 05: Python Intermediate 02

### Question 14 (weight: 1; total: 34)

What is the output of the following code?

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

person = Person(name='Alice', age='30')
print(person)
```

a) A ValidationError is raised
b) `Person(name='Alice', age=30)`
c) `name='Alice' age=30`
d) `Person object`

### Question 15 (weight: 2; total: 36)

What will be the output of the previous code if we add the following line to the `Person` class?

```python
...
    def __str__(self):
        return f'{self.name} is {self.age} years old'
...
```

a) The code will raise a SyntaxError
b) `Person object`
c) `name='Alice' age=30`
d) `Alice is 30 years old`

### Question 16 (weight: 5; total: 41)

What is the output of the following code?

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def __enter__(self):
        print('B')

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('A')

    @property
    def value(self):
        return self._value / 2

with MyClass(10) as obj:
    print(obj.value)
    print('C')
```

a)
```
B
5.0
C
A
```
b)
```
A
10.0
C
B
```
c)
```
5.0
A
C
B
```
d)
```
10.0
C
B
A
```

### Question 17 (weight: 5; total: 46)

A generator is a function that returns an iterator. It looks like a normal function but contains a `yield` statement. The `yield` statement pauses the function and saves the local state of the function. The state is remembered across successive calls. Select the options that correctly defines the main built-in generators in Python:

[] `enumerate` - returns an iterator of tuples containing an index and the value of an iterable
[] `filter` - creates a list of elements for which a function returns true. It must be a `lambda` function
[] `map` - applies a function to all the items in an input list
[] `range` - returns a sequence of positive numbers
[] `zip` - aggregates elements from two or more iterables

---

## Day 06: Models, Comprehension and Databases

### Question 18 (weight: 3; total: 49)

The `dataclass` decorator is a utility that is used to create classes which are primarily used to store data. Accordingly with `dataclass` signature:

```python
def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
              unsafe_hash=False, frozen=False, match_args=True,
              kw_only=False, slots=False):
    ...
```

[] The __init__() method is added to the class by default
[] The __repr__() method is added to the class by default
[] The __eq__() method is added to the class by default
[] The __hash__() method is added to the class by default

### Question 19 (weight: 3; total: 54)

The following code could be replaced by a list comprehension. What is the equivalent list comprehension?

```python
l = [1, 2, 3, 4, 5]

result = []
for i in l:
    if i % 2 == 0:
        result.append(i ** 2)
```

a) `[i ** 2 for i in l if i % 2 == 0]`
b) `[i ** 2 for i in l]`
c) `[i for i in l if i % 2 == 0]`
d) `[i for i in l]`

### Question 20 (weight: 3; total: 57)

The following code is an example of:
    
```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<User(name={self.name})>"
```

a) SQLAlchemy model
b) Pydantic model
c) Django model
d) FastAPI model

---

## Day 07: APIs with FastAPI and Django Rest Framework

### Question 21 (weight: 1; total: 60)

Which library is the following code related to?
    
```python
...
router = APIRouter()
nested_router = APIRouter()

@nested_router.get("/")
def sample():
    return {"response": "sample"}

router.include_router(nested_router, prefix="/nested")
```

a) Django Rest Framework
b) Flask
c) SQLAlchemy
d) FastAPI

### Question 22 (weight: 3; total: 63)

When running the previous code, the developer complains that the `/nested` endpoint is not working. What is the most likely reason?

a) The `nested_router` is not included in the `router`
b) The `router` is not a `GET` method
c) The `nested_router` is not returning a response
d) The `router` is not included in the `app`

### Question 23 (weight: 3; total: 66)

The main difference between FastAPI and Django Rest Framework models is:

a) Django Rest Framework does not have models, only serializers
b) FastAPI models are based on Pydantic models, while Django Rest Framework models are based on Django models
c) FastAPI models can be created using `python manage.py startmodel`, while Django Rest Framework models are created using `poetry add model`
d) Django Rest Framework models are based on Pydantic models, while FastAPI models are based exclusively on dataclasses

### Question 24 (weight: 3; total: 69)

Django Rest Framework relies on the following concepts to create APIs:

a) Serializers, Views and Templates
b) Serializers, Forms and Views
c) Models, Serializers and Views
d) Models, Serializers and Forms

---

## Day 08: Web with Django

### Question 25 (weight: 3; total: 72)

Django relies on the following concepts to create web applications:

a) Serializers, Models and Views
b) Models, Views and Forms
c) Models, Views and Templates
d) Forms, Views and Templates

### Question 26 (weight: 3; total: 75)

Which class is used to create a Django model?

a) The class `Model` from the `django.db.model` module
b) The class `BaseModel` from the `django.db` module
c) The class `Model` from the `django.db` module
d) The class `BaseModel` from the `django.db.model` module

### Question 27 (weight: 3; total: 78)

The developer wants to add a new field to represent a person's job, but he also wants to represent the job's name and description. What is the best way to do this considering that a person can have only one job and a job can have multiple persons?

```python
...

class Person(...):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} is {self.age} years old'
```

a) Create two new fields called `job_name` and `job_description` in the `Person` model
b) Create a new model called `Job` with the desired fields and add a `ForeignKey` field to the `Person` model
c) Create a new model called `Job` with the desired fields and add a `OneToOneField` field to the `Person` model
d) Create a new model called `Job` with the desired fields and add a `ManyToManyField` field to the `Person` model

### Question 28 (weight: 3; total: 81)

After changing the `Person` model to include the `Job` model, the developer is unable to create a new person, because he keeps receiving a `Table ... doesn't exist` error. What is the most likely reason?

a) The developer forgot to run the `makemigrations` and `migrate` commands
b) The `Job` model is not registered in the Django admin
c) The `Job` model is not imported in the `Person` model
d) The field does not have `related_name` attribute set

---

## Day 09: Debug, Logging, Tests and Error Handling

### Question 29 (weight: 1; total: 82)

What is the output of the following code?

```python
import logging

logging.basicConfig(level=logging.DEBUG)

def my_func(a, b):
    logging.debug(f'a: {a}, b: {b}')
    return a + b

result = my_func(10, 20)
print(result)
```
a) `30`
b) `a: 10, b: 20`
c)
```
a: 10, b: 20
30
```
d)
```
DEBUG:root:a: 10, b: 20
30
```

### Question 30 (weight: 3; total: 85)

What is the output of the following code?

```python
def my_func(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return 'Division by zero'

    finally:
        return 'Finally'

result = my_func(10, 0)
print(result)
```

a) `Division by zero`
b) `Finally`
c) `Division by zero` and `Finally`
d) `Finally` and `Division by zero`

---

## Final Questions

### Question 31 (weight: 5; total: 90)

Based on the following code:

```python
import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
df["A"] = df["A"].apply(lambda x: x * 2)

A = df

df["B"] = df["B"].map({4: "four", 5: "five", 6: "six"})

B = df

grouped_df = df.groupby("C")["A"].sum()

C = grouped_df

sorted_df = df.sort_values("B", ascending=False)

D = sorted_df

df_1 = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9],
    }
)
df_2 = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [7, 8, 9],
        "C": [10, 11, 12],
    }
)

merged_df = pd.merge(df_1, df_2, left_on=["A"], right_on=["A"])

E = merged_df

merged_df.columns = ["A", "B_1", "C_1", "B_2", "C_2"]

F = merged_df
```

Select the options that are correct:

[] The dataframe object `A` is the same as the dataframe object `B`
[] The dataframe object `C` is as follows:
```
C
7    4
8    6
9    8
Name: A, dtype: int64
```
[] The dataframe object `D` is the sorted dataframe by the column `B` in ascending order
[] The dataframe object `E` is the result of merging two dataframes based on the column `A`
[] The dataframe object `F` is as follows:
```
A  B_1  C_1  B_2  C_2
0  1    4    7    7   10
1  2    5    8    8   11
2  3    6    9    9   12
```

### Question 32 (weight: 5; total: 95)

Based on the following code:

```python
import click

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
```

Select the options that are correct:

[] The `cli` function is a group of commands, that means it is a command that has subcommands
[] To define an option for the `initdb` command, the developer should use the `@click.option` decorator
[] It is possible to build a .whl file from this code using Poetry by running the command `poetry create`, but we need to add `tool.poetry.scripts` to the `pyproject.toml` file passing the command name and the path to the function
[] With the .whl file built, the developer can install the package using the command `pip install <package-name>.whl`

### Question 33 (weight: 5; total: 100)

Based on the following code:

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data_a = response.json()
A = data_a['title']

response = requests.get('https://jsonplaceholder.typicode.com/posts/2')
B = response.status_code
data_b = response.json()
C = data_b['id']

```

Select the options that are correct:

[] The variable `C` is the title of the GET request to the post with id 2
[] The variable `A` is the title of the GET request to the post with id 1
[] The variable `B` is the status code of the request to the post with id 2
[] The variable `C` is the id of the GET request to the post with id 1
[] The variable `A` is the status code of the request to the post with id 1
```
