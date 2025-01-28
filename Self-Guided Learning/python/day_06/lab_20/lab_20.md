# Lab 20: Data Classes

In this lab, you will create a data class to represent a `Person` with attributes: 

- `name` (str)
- `age` (int)
- `job` (Job | None) = None

The `job` attribute will be default `None` or another data class called `Job` with two attributes:

- `title` (str)
- `salary` (float)

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `data_class.py`.
2. In `data_class.py`, create a data class called `Job` with two attributes: `title` (str) and `salary` (float).

```python
from dataclasses import dataclass

@dataclass
class Job:
    title: str
    salary: float
```

3. In `data_class.py`, create a data class called `Person` with three attributes: `name` (str), `age` (int) and `job` (Job | None).

```python
...

@dataclass
class Person:
    name: str
    age: int
    job: Job | None = None
```

4. In `data_class.py`, instantiate a `Person` object with the following attributes:

### Example

```python
...

software_engineer = Job(title="Software Engineer", salary=100000)
person = Person(name="Alice", age=30, job=software_engineer)
print(person)
```

5. Run the script and observe the output.

### Optional Challenge

- Create another attribute in the `Person` class called `friends` that is a list of `Person` objects.
- Add a method to the `Person` class called `add_friend` that appends a `Person` object to the `friends` list.
- Add a method to the `Person` class called `remove_friend` that removes a `Person` object from the `friends` list.
- Create another attribute in the `Person` class called `pet` that is default `None` or another data class called `Pet` with two attributes: `name` (str) and `species` (str).
- Add a method to the `Person` class called `add_pet` that sets the `pet` attribute to a `Pet` object.
- Add a method to the `Person` class called `remove_pet` that sets the `pet` attribute to `None`.