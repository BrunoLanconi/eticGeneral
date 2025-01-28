# Lab 18: Context Management

In this lab, you will learn how to use context management in Python. You will create a class that uses the `__enter__` and `__exit__` methods to manage the context of the class.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `main.py`.

```python
class ContextManager:
    def __enter__(self):
        print('Entering the context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting the context')

with ContextManager() as cm:
    print('Inside the context')
```

2. Run the Python file and observe the output.
3. Create a conditional statement inside the `__exit__` method to check if an exception occurred. If an exception occurred, print the exception message. If no exception occurred, print a message saying that no exception occurred.

```python
class ContextManager:
    def __enter__(self):
        print('Entering the context')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f'An exception occurred: {exc_value}')
        else:
            print('No exception occurred')
        print('Exiting the context')

...
```

4. Raise an exception inside the context and observe the output.

```python
...

with ContextManager() as cm:
    print('Inside the context')
    raise Exception('An error occurred')
```

5. Change `ContextManager`class to `FileContextManager` and make it reads a file in the `__enter__` method and closes the file in the `__exit__` method.

```python
class FileContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

...
```

6. Create a new file called `sample.txt` and write some text to it.
7. Use the `FileContextManager` class to read the contents of the file.

```python
with FileContextManager('sample.txt') as file:
    print(file.read())
```

8. Run the Python file and observe the output.

**Trivia**: We may also use `open` function as a context manager. The `open` function returns a file object that can be used as a context manager. The file is automatically closed when the context manager exits.

```python
with open('sample.txt', 'r') as file:
    print(file.read())
```

9. Let's guarantee that our file is closed even if an exception occurs. Add a `try` and `finally` block to the `__exit__` method.

```python
class FileContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.file.close()
        finally:
            print('File closed')

...
```

10. Raise an exception inside the context and observe the output.

```python
...

with FileContextManager('sample.txt') as file:
    print(file.read())
    raise Exception('An error occurred')
```

11. Run the Python file and observe the output.
12. Remove the `FileContextManager` class and use the `contextlib` module to create a context manager that reads a file.

```python
from contextlib import contextmanager

@contextmanager
def file_context_manager(filename):
    file = open(filename, 'r')
    try:
        yield file
    finally:
        file.close()

...
```

13. Use the `file_context_manager` function to read the contents of the file.

```python
with file_context_manager('sample.txt') as file:
    print(file.read())
```
