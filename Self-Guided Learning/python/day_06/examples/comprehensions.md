# Comprehensions

Comprehensions are a concise way to create collections in Python. They are a way to build a new collection by iterating over an existing collection and applying an operation to each element. There are four types of comprehensions in Python:

- List comprehensions
- Set comprehensions
- Dictionary comprehensions
- Generator comprehensions

---

## [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

List comprehensions provide a concise way to create lists. They consist of square brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new list resulting from evaluating the expression in the context of the `for` and `if` clauses that follow it.

### Example
```python
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

In the example above, the list comprehension creates a list of squares of numbers from 0 to 9.

---

## [Set Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#sets)

Set comprehensions provide a concise way to create sets. They consist of curly braces containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new set resulting from evaluating the expression in the context of the `for` and `if` clauses that follow it.

### Example
```python
squares = {x ** 2 for x in range(10)}
print(squares)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

In the example above, the set comprehension creates a set of squares of numbers from 0 to 9.

---

## [Dictionary Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

Dictionary comprehensions provide a concise way to create dictionaries. They consist of curly braces containing key-value pairs separated by a colon followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new dictionary resulting from evaluating the expression in the context of the `for` and `if` clauses that follow it.

### Example
```python
squares = {x: x ** 2 for x in range(10)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

In the example above, the dictionary comprehension creates a dictionary of squares of numbers from 0 to 9.

---

## [Generator Comprehensions](https://docs.python.org/3/tutorial/classes.html#generators)

Generator comprehensions provide a concise way to create generators. They consist of parentheses containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new generator resulting from evaluating the expression in the context of the `for` and `if` clauses that follow it.

### Example
```python
squares = (x ** 2 for x in range(10))
print(squares)  # <generator object <genexpr> at 0x7f8b1c6b3d60>
```

In the example above, the generator comprehension creates a generator of squares of numbers from 0 to 9.

---

### Generators

Generators are a type of iterable, like lists or tuples. They allow you to iterate over a sequence of values without storing them in memory. Generators are created using generator expressions or functions with the `yield` keyword.

### Example
```python
from typing import Generator


def square_numbers(n: int) -> Generator[int, None, None]:
    for i in range(n):
        yield i ** 2

squares = square_numbers(10)
print(squares)  # <generator object square_numbers at 0x7f8b1c6b3d60>
```

**Note**: The type hint may look a bit different - this is because of `yield` keyword presence. `yield` is a special keyword presence defines the function as a generator function. When a generator function is called, it returns a generator object that can be used to iterate over the values produced by the generator function - in other words, `yield` returns a `Generator` with three type arguments:

- The first argument is the type of the values that the generator yields.
- The second argument is the type of the value that the generator can receive from the caller.
- The third argument is the type of the value that the generator can return.

Generators are useful when you need to iterate over a large sequence of values without storing them in memory and when you know how to generate the values on the fly.

Here is an example of a `Generator` that can receive a value from the caller and return a value to the caller:

```python
from typing import Generator


def my_generator(n: int) -> Generator[int, int, str]:
    """
    A generator function that yields integers from 0 to n-1 and receives values from the caller.
    Args:
        n (int): The upper limit of the range.
    Yields:
        int: The next integer in the range.
    Receives:
        int: The value sent by the caller.
    Return:
        str: A message indicating the last value received.
    """
    for i in range(n):
        x = yield i

        print(f"From caller: {x}")

    return f"The last from caller: {x}"


def main():
    """
    This function demonstrates the usage of a generator.

    It creates a generator object using the `my_generator` function and calls `next()` on it to initialize the generator.
    Then, it enters a loop where it sends a value to the generator using `generator.send()` and increments the value by 10.
    The loop continues until a `StopIteration` exception is raised, at which point the value of the exception is printed.
    """
    generator = my_generator(10)
    next(generator)

    try:
        n = 0
        while True:
            response = generator.send(n)

            print(f"From generator: {response}")

            n += 10

    except StopIteration as e:
        print(e.value)


if __name__ == "__main__":
    main()
```

This should output:

```
From caller: 0
From generator: 1
From caller: 10
From generator: 2
From caller: 20
From generator: 3
From caller: 30
From generator: 4
From caller: 40
From generator: 5
From caller: 50
From generator: 6
From caller: 60
From generator: 7
From caller: 70
From generator: 8
From caller: 80
From generator: 9
From caller: 90
The last from caller: 90
```