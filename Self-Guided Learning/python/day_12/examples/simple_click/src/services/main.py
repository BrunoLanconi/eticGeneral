"""
This file specifies the services core.
"""

from src.services.log import logger, log


def main_service():
    """
    Logs welcome message
    """
    logger.debug("This is a DEBUG level message!")
    logger.info("Your template for simple_click project is complete!")
    log.custom("This is a CUSTOM level message!")
