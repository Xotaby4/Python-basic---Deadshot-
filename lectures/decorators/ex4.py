from functools import wraps


def decor(func):
    @wraps(func)
    def wrap():
        func()
    # wrap.__name__ = func.__name__
    return wrap


@decor
def func():
    pass


# wraped_func_1 = decor(func)
# wraped_func_1()

# func()

print(func.__name__)
