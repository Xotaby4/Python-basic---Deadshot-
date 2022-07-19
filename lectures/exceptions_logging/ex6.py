import logging

logging.basicConfig(level=logging.ERROR, filename="test.log", filemode="w",
                    format="%(levelname)s||%(asctime)s||%(pathname)s - %(message)s")

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')