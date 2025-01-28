"""
This file specifies general logging script.
"""

import logging
import os.path
import sys
from pathlib import Path

"""
How to add custom levels and custom log files:
1) Add custom level at # Custom levels;
2) Add custom file handler at # Handlers;
3) Subscribe custom level at # Subscribe custom level;
4) Create logging staticmethod as # Sample custom logging staticmethod;
5) Add it at Sample logging function and test.
"""


class Log(logging.getLoggerClass()):
    # Custom levels
    CUSTOM_LEVEL = 21

    def __init__(self, log_level: int, target_folder: str):
        """
        A class grouping logger and handlers for logging process

        :param log_level: an int representing the log level to be used by default logger
        :param target_folder: a str representing the folder to create logs folder
        """
        self.log_path = os.path.join(target_folder, "logs")
        self.logger = logging.getLogger()
        self.formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        self.logger.setLevel(log_level)
        os.makedirs(self.log_path, exist_ok=True)

        # Handlers
        self._errors_file()
        self._logs_file()
        self._custom_file()
        self._stdout()
        self._stderr()

        # Subscribe custom level
        self._add_logging_name(level_name="CUSTOM", level_number=self.CUSTOM_LEVEL)

        super(Log, self).__init__(name="logger", level=log_level)

    def _errors_file(self):
        """
        Sets an errors file handler for ERROR level
        """
        errors_filename = "errors.log"
        errors_file_path = os.path.join(self.log_path, errors_filename)
        errors_file_handler = logging.FileHandler(errors_file_path, "a", "utf-8")

        self._add_to_logger(handler=errors_file_handler, logging_level=logging.ERROR)

    def _logs_file(self):
        """
        Sets a logs file handler for ANY level
        """
        logs_filename = "logs.log"
        logs_file_path = os.path.join(self.log_path, logs_filename)
        logs_file_handler = logging.FileHandler(logs_file_path, "a", "utf-8")

        self._add_to_logger(handler=logs_file_handler, logging_level=logging.DEBUG)

    def _custom_file(self):
        """
        Sets custom level name and sets a dependents file handler for custom level
        """
        custom_filename = "custom.log"
        custom_file_path = os.path.join(self.log_path, custom_filename)
        custom_file_handler = logging.FileHandler(custom_file_path, "a", "utf-8")

        # Filtering
        custom_file_handler.addFilter(
            lambda record: record.levelno == self.CUSTOM_LEVEL
        )
        self._add_to_logger(
            handler=custom_file_handler, logging_level=self.CUSTOM_LEVEL
        )

    def _stdout(self):
        """
        Sets a stdout handler for DEBUG level
        """
        stdout_handler = logging.StreamHandler(sys.stdout)

        # Filtering
        stdout_handler.addFilter(lambda record: record.levelno <= logging.WARNING)
        self._add_to_logger(handler=stdout_handler, logging_level=logging.DEBUG)

    def _stderr(self):
        """
        Sets a stderr handler for ERROR level
        """
        stderr_handler = logging.StreamHandler(sys.stderr)

        self._add_to_logger(handler=stderr_handler, logging_level=logging.ERROR)

    def _add_to_logger(self, handler: logging.StreamHandler, logging_level: int):
        """
        Adds handler to object logger

        :param handler: a StreamHandler object representing handler to be added
        :param logging_level: an int representing the handler default logging level
        """
        handler.setLevel(logging_level)
        handler.setFormatter(self.formatter)
        self.logger.addHandler(handler)

    @staticmethod
    def _add_logging_name(
        level_name: str, level_number: int, method_name: str | None = None
    ):
        """
        Comprehensively adds a new logging level to the `logging` module and the
        currently configured logging class.
        https://stackoverflow.com/questions/2183233/how-to-add-a-custom-loglevel-to-pythons-logging-facility/35804945#35804945

        :param level_name: a str representing the level name
        :param level_number: an int representing the level number
        :param method_name: a str representing the method name
        """
        if not method_name:
            method_name = level_name.lower()

        logger_class = logging.getLoggerClass()

        if hasattr(logging, level_name):
            raise AttributeError(f"{level_name} already defined in logging module")
        if hasattr(logging, method_name):
            raise AttributeError(f"{method_name} already defined in logging module")
        if hasattr(logger_class, method_name):
            raise AttributeError(f"{method_name} already defined in logger class")

        def log_to_root(message, *args, **kwargs):
            logging.log(level_number, message, *args, **kwargs)

        logging.addLevelName(level_number, level_name)
        setattr(logging, level_name, level_number)
        setattr(logging, method_name, log_to_root)

    @staticmethod
    def custom(message):  # Sample custom logging staticmethod
        """
        Logs {message} on custom level

        :param message: a str representing the message to log
        """
        # Pycharm can't identify functions programmatically implemented
        logging.custom(message)  # type: ignore

    def __call__(self, *args, **kwargs) -> logging.Logger:
        """
        :return: a Logger object representing the logger
        """
        return self.logger


log = Log(log_level=logging.INFO, target_folder=f"{str(Path.home())}/.simple_click")
logger = log()


# System except hook
# https://stackoverflow.com/questions/8050775/using-pythons-logging-module-to-log-all-exceptions-and-errors
sys.excepthook = lambda t, v, tb: logger.exception(f"Uncaught exception: {v}.")


def main():
    """
    Sample logging function
    """
    logger.debug("Debug")
    logger.info("Info")
    log.custom("Custom")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical")
    raise SystemError("Sample uncaught exception")


if __name__ == "__main__":
    main()
