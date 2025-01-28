# Lab 30: Files

In this lab, you will learn how to read and write files in Python. You will create a function that reads a file and prints its content.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `main.py`.
2. Create a function called `read_file` that reads a file and prints its content.

```python
def read_file(filename: str) -> str:
    """
    Read a file and return its content.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    with open(filename, 'r') as file:
        content = file.read()
        
    return content

print(read_file('sample.txt'))
```

3. Create a file called `sample.txt` with the following content:

```
Hello, World!
```

4. Run the Python file and observe the output.
5. Change the `read_file` function to accept a file object instead of a filename.

```python
from typing import TextIO

def read_file(file: TextIO) -> str:
    """
    Read a file and return its content.

    Args:
        filename (TextIO): The file object to read.
    
    Returns:
        str: The content of the file.
    """
    content = file.read()
        
    return content

with open('sample.txt', 'r') as file:
    print(read_file(file))
```

6. Run the Python file and observe the output.
7. Create a function called `write_file` that writes a string to a file.

```python
def write_file(filename: str, content: str) -> None:
    """
    Write content to a file.

    Args:
        filename (str): The name of the file to write.
        content (str): The content to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)

write_file('output.txt', 'Hello, Output!')

with open('output.txt', 'r') as file:
    print(file.read())
```

8. Run the Python file and observe the output.
9. Change the `write_file` function to append content to a file instead of overwriting it.

```python
def write_file(filename: str, content: str) -> None:
    """
    Append content to a file.

    Args:
        filename (str): The name of the file to write.
        content (str): The content to append to the file.
    """
    with open(filename, 'a') as file:
        file.write(content)

write_file('output.txt', '\nHello, Again!')

with open('output.txt', 'r') as file:
    print(file.read())
```

10. Run the Python file and observe the output.

---

Your `main.py` file should look like this:

```python
from typing import TextIO

def read_file(file: TextIO) -> str:
    """
    Read a file and return its content.

    Args:
        filename (TextIO): The file object to read.
    """
    content = file.read()
        
    return content

def write_file(filename: str, content: str) -> None:
    """
    Append content to a file.

    Args:
        filename (str): The name of the file to write.
        content (str): The content to append to the file.
    """
    with open(filename, 'a') as file:
        file.write(content)

with open('sample.txt', 'r') as file:
    print(read_file(file))

write_file('output.txt', '\nHello, Again!')

with open('output.txt', 'r') as file:
    print(file.read())
```

**Note**: This is not the perfect way to handle file operations. This is just to show you the basics of reading and writing files in Python. In a real-world scenario, you should handle exceptions, check for file existence, and close the file properly. For example:

```python
def read_file(filename: str) -> str:
    """
    Read a file and return its content.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f'File {filename} not found.')
        content = ''
        
    return content
```

**Note**: In the future, we will learn about exception and logging handling in Python - and you will be able to handle things more gracefully, as below:

```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def read_file(filename: str) -> str:
    """
    Read a file and return its content.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as file:
            logger.info(f'Reading file {filename}')
            content = file.read()

    except FileNotFoundError:
        logger.error(f'File {filename} not found.')
        content = ''
        
    return content
```

### Optional Challenge

- Create a function to create a CSV file with at least 5 rows of data.
- Create a function to read the CSV file and print its content.
- Create a function to append a new row of data to the CSV file.
