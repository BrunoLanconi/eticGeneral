# [Logging](https://docs.python.org/3/library/logging.html)

Python has a built-in logging module that allows you to log messages to a file or the console. It is a more flexible and powerful alternative to `print()`.

### Example
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

The code above will output the log messages to the console. You can also log to a file by specifying the `filename` parameter in the `basicConfig()` function.

### Example
```
DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
```

---

## [Loggers](https://docs.python.org/3/library/logging.html#logger-objects)

The best practice is to create a logger object and use it to log messages. This way, you can configure the logger and handlers separately.

### Example
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

The code above will output the log messages to a file named `example.log`. Since we set the logger level to `DEBUG`, all messages will be logged. The logger level can be set to `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL` and only messages with a level greater than or equal to the logger level will be logged.

By setting `logger = logging.getLogger(__name__)`, you can also create a logger object in a module and use it to log messages. This way, you can configure the logger and handlers separately.

---

## [Handlers](https://docs.python.org/3/library/logging.html#handler-objects)

Handlers are responsible for dispatching the log messages to the appropriate destination. You can add multiple handlers to a logger.

### Example
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('example.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

The code above will output the log messages to both the console and a file named `example.log`. You may set some rules to specify how the messages will be handled. For example, you can set the formatter, the level, and the destination of the messages.

Below all messages goes to `all.log` file and only `ERROR` and `CRITICAL` messages goes to `error.log` file.

### Example
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('all.log')
file_handler.setFormatter(formatter)

error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(error_handler)

logger.debug('This message goes to all.log')
logger.info('This message goes to all.log')
logger.warning('This message goes to all.log')
logger.error('This message goes to all.log and error.log')
logger.critical('This message goes to all.log and error.log')
```

---

## [Formatters](https://docs.python.org/3/library/logging.html#formatter-objects)

Formatters are responsible for formatting the log messages. You can create custom formatters to format the messages as you wish.

### Example
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

...

logger.debug('This is a debug message')
```

The code above will output the log messages with the following format:

### Example
```
2021-07-01 12:00:00,000 - __main__ - DEBUG - This is a debug message
```

You can customize the format by changing the string passed to the `Formatter` constructor. Below are some of the most common format specifiers:

- `%(asctime)s`: The time the log message was created.
- `%(name)s`: The name of the logger used to log the message.
- `%(levelname)s`: The level of the log message.
- `%(message)s`: The log message itself.
- `%(filename)s`: The filename where the log message was logged.
