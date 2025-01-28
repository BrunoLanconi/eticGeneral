import logging
from os.path import join, dirname

logs_folder = join(dirname(__file__), "logs")
all_path = join(logs_folder, "all.log")
error_path = join(logs_folder, "error.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler(all_path)
file_handler.setFormatter(formatter)

error_handler = logging.FileHandler(error_path)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(error_handler)

logger.debug("This message goes to all.log")
logger.info("This message goes to all.log")
logger.warning("This message goes to all.log")
logger.error("This message goes to all.log and error.log")
logger.critical("This message goes to all.log and error.log")
