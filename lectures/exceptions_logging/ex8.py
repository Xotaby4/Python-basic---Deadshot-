import logging
from logging.handlers import SMTPHandler


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test.log", mode="w")
file_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
