#  staticmethod

def mul(a, b):
    return a * b


class Calc:
    @staticmethod
    def sum(a, b):
        return a + b

    def minus(self, a, b):
        return a - b


Calc.sum(1, 2)
calc = Calc()


class User:
    def __init__(self, phone):
        self.phone = phone
        # 067-3434-324-2

    @staticmethod
    def parse_phone(phone):
        # TODO implement
        return phone

    @classmethod
    def test(cls):
        cls.parse_phone()


phone = "1234576457"
