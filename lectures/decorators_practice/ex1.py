

def decorator_print(func):
    def wrap(a, b):
        res = func(a, b)
        print(f"{a} + {b} = {res}")
        return res
    return wrap


class FunctorDecoratorPrint:
    def __call__(self, func):
        def wrap(a, b):
            res = func(a, b)
            print(f"{a} + {b} = {res}")
            return res
        return wrap

# my_decor = FunctorDecoratorPrint()

# @decorator_print
@FunctorDecoratorPrint()
def sum(a, b):
    return a + b


sum(1, 1)
sum(1, 2)
sum(3, 2)