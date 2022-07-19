import logging
a = 5
b = 0

logging.basicConfig(level=logging.ERROR, filename="test.log", filemode="w")
try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
