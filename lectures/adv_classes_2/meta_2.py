import time


def decorator_timer(func):
    def wrap(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        print(time.time() - t1)
        return result
    return wrap


@decorator_timer
def test():
    pass


step_1 = decorator_timer(test)
step_1(1, 2, 3, 4)


class DecorMetaclass(type):

    def __new__(cls, name, bases, dct):

        for key, value in dct.items():
            if callable(value):
                dct[key] = decorator_timer(value)

        return super(DecorMetaclass, cls).__new__(cls, name, bases, dct)


class MyClass(metaclass=DecorMetaclass):
    def func_1(self):
        time.sleep(1)

    def func_2(self):
        time.sleep(3)


m = MyClass()
m.func_1()
m.func_2()