import time


def decor(decor_arg):
    def timer(func):
        def wrap(*args, **kwargs):
            t1 = time.time()
            result = func(*args, **kwargs)
            print(time.time() - t1)
            return result

        return wrap
    return timer




# @timer
# def func_2(a):
#     time.sleep(2)
#
#
# timer = decor(1)
# wrap_out = timer(func_2)
# wrap_out(1, 2)
#
# print(func(1, 2))
# print(func_2(1))


class Functor:
    def __init__(self, arg_1):
        self.arg_1 = arg_1

    def method(self):
        pass

    def __call__(self, func):
        def wrap(*args, **kwargs):
            self.method()
            t1 = time.time()
            if self.arg_1 == 2:
                print("111")
            result = func(*args, **kwargs)
            print(time.time() - t1)
            return result
        return wrap


@Functor(2)
def func(a, b):
    time.sleep(1)
    return a + b

func(1, 2)
