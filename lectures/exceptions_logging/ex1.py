"""
-project
--api
---expections.py
--models
---expections.py
--parsers
---expections.py
--expections.py
"""


class MyException(Exception):
    pass


class MyException1(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message


raise MyException("message", 1, 2)
