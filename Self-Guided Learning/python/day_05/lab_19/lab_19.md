# Lab 19: Generators and Decorators

In this lab, you will learn how to use generators and decorators in Python. You will create a generator that generates a sequence of numbers and a decorator that prints the time it takes to run a function.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `main.py`.
2. Create a generator function called `generate_numbers` that generates a sequence of numbers from 1 to 10.

```python
def generate_numbers():
    for i in range(1, 11):
        yield i
```

3. Create a for loop that iterates over the generator and prints each number.

```python
for number in generate_numbers():
    print(number)
```

4. Create a decorator function called `timeit` that prints the time it takes to run a function.

```python
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time taken to run {func.__name__}: {end_time - start_time} seconds')
        return result
    return wrapper
```

5. Decorate the `generate_numbers` function with the `timeit` decorator.

```python
@timeit
def generate_numbers():
    for i in range(1, 11):
        yield i
```

6. Run the Python file and observe the output.
7. Create a new function called `generate_fibonacci` that generates a sequence of Fibonacci numbers.

```python
@timeit
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

8. Create a for loop that iterates over the generator and prints each Fibonacci number.

```python
for number in generate_fibonacci(10):
    print(number)
```

9. Run the Python file and observe the output.
10. Create a new decorator function called `logit` that logs the arguments and return value of a function.

```python
def logit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Arguments: {args}, {kwargs}')
        print(f'Return value: {result}')
        return result
    return wrapper
```

11. Decorate the `generate_fibonacci` function with the `logit` decorator.

```python
@logit
@timeit
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

12. Run the Python file and observe the output.
13. Add some additional print statements to the decorator functions to check the order of execution.

```python
def timeit(func):
    def wrapper(*args, **kwargs):
        print('Timeit decorator start')
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time taken to run {func.__name__}: {end_time - start_time} seconds')
        print('Timeit decorator end')
        return result
    return wrapper

def logit(func):
    def wrapper(*args, **kwargs):
        print('Logit decorator start')
        result = func(*args, **kwargs)
        print(f'Arguments: {args}, {kwargs}')
        print(f'Return value: {result}')
        print('Logit decorator end')
        return result
    return wrapper
```

14. Run the Python file and observe the output.
15. Experiment with different combinations of decorators and observe the order of execution.
16. Let's add an argument to the `timeit` decorator to specify the unit of time.

```python
def timeit(unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if unit == 'seconds':
                print(f'Time taken to run {func.__name__}: {end_time - start_time} seconds')
            elif unit == 'milliseconds':
                print(f'Time taken to run {func.__name__}: {(end_time - start_time) * 1000} milliseconds')
            else:
                raise NotImplementedError(f'Unit {unit} is not supported')
            return result
        return wrapper
    return decorator
```

17. Decorate the `generate_fibonacci` function with the `timeit` decorator specifying the unit as `milliseconds`.

```python
@timeit(unit='milliseconds')
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

18. Run the Python file and observe the output.
19. Experiment with different units of time and observe the output.

---

Your final `main.py` file should look like this:

```python
import time

def timeit(unit='seconds'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if unit == 'seconds':
                print(f'Time taken to run {func.__name__}: {end_time - start_time} seconds')
            elif unit == 'milliseconds':
                print(f'Time taken to run {func.__name__}: {(end_time - start_time) * 1000} milliseconds')
            else:
                raise NotImplementedError(f'Unit {unit} is not supported')
            return result
        return wrapper
    return decorator

def logit(func):
    def wrapper(*args, **kwargs):
        print('Logit decorator start')
        result = func(*args, **kwargs)
        print(f'Arguments: {args}, {kwargs}')
        print(f'Return value: {result}')
        print('Logit decorator end')
        return result
    return wrapper

@timeit
def generate_numbers():
    for i in range(1, 11):
        yield i
    
@logit
@timeit(unit='milliseconds')
def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in generate_numbers():
    print(number)

for number in generate_fibonacci(10):
    print(number)
```