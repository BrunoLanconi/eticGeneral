## Python Modules

A module is simply a file containing Python definitions and statements. Here's an example of a simple module:

### Example
```python
# my_module.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

You can import and use this module in another Python script:

### Example
```python
# main.py

import my_module

print(my_module.greet("Alice"))
print(my_module.add(3, 4))
```

---

## [os Module](https://docs.python.org/3/library/os.html)

The `os` module provides a way of using operating system dependent functionality like reading or writing to the file system. Below are some common operations using the `os` module:


### Example
```python
import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# List files and directories in the current directory
files = os.listdir(cwd)
print(f"Files and Directories in '{cwd}': {files}")

# Create a new directory
new_dir = os.path.join(cwd, "new_folder")
os.makedirs(new_dir, exist_ok=True)
print(f"Created Directory: {new_dir}")

# Rename a directory or file
os.rename("new_folder", "renamed_folder")
print("Directory renamed to 'renamed_folder'")

# Remove a directory
os.rmdir("renamed_folder")
print("Removed Directory: 'renamed_folder'")
```

### Example
```python
import os

# Get the value of an environment variable
path = os.getenv("PATH")
print(f"PATH: {path}")

# Set the value of an environment variable
os.environ["MY_VARIABLE"] = "some_value"
print(f"MY_VARIABLE: {os.getenv('MY_VARIABLE')}")
```

---

## [sys Module](https://docs.python.org/3/library/sys.html)

The `sys` module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

### Example
```python
import sys

# Print the command-line arguments
print(f"Command-Line Arguments: {sys.argv}")

# Access individual arguments
if len(sys.argv) > 1:
    print(f"First Argument: {sys.argv[1]}")
else:
    print("No command-line arguments provided")
```

### Example
```python
import sys

# Exit the program with a status code
sys.exit(0)
```

### Example
```python
import sys

# Print to standard output
# NOTE Better logging will be covered in Day 09
sys.stdout.write("This is standard output\n")

# Print to standard error
sys.stderr.write("This is standard error\n")

# Read from standard input
print("Enter some text:")
input_text = sys.stdin.readline().strip()
print(f"You entered: {input_text}")
```
