# Files

In Python, we can work with files using the built-in `open()` function. This function returns a file object that we can use to read or write data to a file. The `open()` function takes two arguments: the file path and the mode in which we want to open the file.

---

## [Open](https://docs.python.org/3/library/functions.html#open)

The `open()` function opens a file and returns a file object. The file object can be used to read, write, or append data to the file.

### Example
```python
file = open(`sample.txt`, `r`)
```

The first argument to the `open()` function is the file path, and the second argument is the mode in which we want to open the file. The mode can be one of the following:

- `r`: open for reading (default)
- `w`: open for writing, truncating the file first
- `x`: open for exclusive creation, failing if the file already exists
- `a`: open for writing, appending to the end of file if it exists
- `b`: binary mode
- `t`: text mode (default)
- `+`: open for updating (reading and writing)

The default mode is `r` (open for reading text, a synonym of `rt`). Modes `w+` and `w+b` open and truncate the file. Modes `r+` and `r+b` open the file with no truncation.

---

## [Read](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

To read the contents of a file, we can use the `read()` method of the file object. This method reads the entire file and returns its contents as a string.

### Example
```python
file = open(`sample.txt`, `r`)
content = file.read()

print(content)
file.close()
```

But this approach is not recommended because we have to remember to close the file after reading it. A better approach is to use the `with` statement, which automatically closes the file when the block is exited.

### Example
```python
with open(`sample.txt`, `r`) as file:
    content = file.read()
    
    print(content)
```

---

## [Write](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

To write data to a file, we can use the `write()` method of the file object. This method writes the specified data to the file.

### Example
```python
with open(`sample.txt`, `w`) as file:
    file.write(`Hello, World!`)
```

---

## [Append](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

To append data to a file, we can use the `a` mode when opening the file. This mode allows us to write data to the end of the file without truncating it.

### Example
```python
with open(`sample.txt`, `a`) as file:
    file.write(`Hello, World!`)
```
