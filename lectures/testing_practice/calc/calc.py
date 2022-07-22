class Calc:
    @staticmethod
    def sum(*args):
        res = 0
        for i in args:
            res += i
        return res

    @staticmethod
    def div(a, b):
        return

    @staticmethod
    def mul(a, b):
        return

    @classmethod
    def avg(cls, *args):
        sum_res = cls.sum(*args)
        return sum_res / len(args)
