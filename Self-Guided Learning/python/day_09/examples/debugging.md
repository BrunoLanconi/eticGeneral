# [Debugging](https://docs.python.org/3/library/pdb.html)

Python has a built-in debugger called `pdb`. It allows you to step through your code and inspect variables at each step. To use it, you can insert the following line in your code:

### Example
```python
import pdb; pdb.set_trace()
```

You also may use `breakpoint()` instead of `import pdb; pdb.set_trace()`.

### Example
```python
breakpoint()
```

---

## [Commands](https://docs.python.org/3/library/pdb.html#debugger-commands)

When you run your code, it will pause at that line, then you may then use some commands to navigate through your code. See some of the most common commands below:

- `n` or `next`: Execute the current line and move to the next line.
- `c` or `continue`: Continue execution
- `q` or `quit`: Quit the debugger and the program
- `p` or `print`: Print the value of a variable
- `s` or `step`: Step into a function
- `h` or `help`: Show a list of commands
- `w` or `where`: Show the current stack trace
