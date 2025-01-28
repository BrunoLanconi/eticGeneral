# Lab 27: Create a Logger

In this lab, you will learn how to create a simple logger in Python using `logging` module. This logger will log messages to a file and the console.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `logger.py`.

```bash
$ touch logger.py
```

2. In the `logger.py` file, import the `logging` module and create a logger object.

```python
import logging

logger = logging.getLogger(__name__)
```

This is pretty much the standard way to create a logger object in Python. The `__name__` variable is a special variable in Python that contains the name of the current module. This is useful when you want to create a logger for a specific module.

3. Set the logging level to `DEBUG`.

```python
logger.setLevel(logging.DEBUG)
```

This will set the logging level to `DEBUG`, which means that all messages will be logged.

4. Create a formatter object.

```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

This formatter object will format the log messages in the following way:

```
2021-07-01 12:00:00,000 - __main__ - DEBUG - This is a debug message
```

5. Create a file handler object and set the formatter.

```python
file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
```

This will create a file handler object that will log messages to a file called `app.log` and set the formatter to the formatter object we created earlier.

6. Define the logging level for the file handler to `ERROR`.

```python
file_handler.setLevel(logging.ERROR)
```

This will set the logging level for the file handler to `ERROR`, which means that only messages with a level of `ERROR` or higher will be logged to the file.

7. Create a console handler object and set the formatter.

```python
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
```

This will create a console handler object that will log messages to the console and set the formatter to the formatter object we created earlier.

8. Add the file handler and console handler to the logger object.

```python
logger.addHandler(file_handler)
logger.addHandler(console_handler)
```

Logging handlers are used to send log messages to specific destinations. In this case, we are adding the file handler and console handler to the logger object. The file handler will log messages to a file, and the console handler will log messages to the console.

9. Log some messages.

```python
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

Your final `logger.py` file should look like this:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('app.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

10. Run the `logger.py` file.

### Optional Challenge

- Create a `Logger` class that encapsulates the logger functionality and can be reused in other modules.