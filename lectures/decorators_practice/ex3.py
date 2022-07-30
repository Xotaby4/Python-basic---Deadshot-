def decorator(flag):
    def big_wrap(func):
        def wrap_1(a, b):
            res = func(a, b)
            print(f"{a} + {b} = {res}")
            return res

        def wrap_2(a, b):
            res = func(a, b)
            print(res)
            return res

        if flag:
            return wrap_1
        else:
            return wrap_2

    return big_wrap


class FunctorDecor:
    def __init__(self, flag):
        self.flag = flag
        self.__wrapped_func = None

        self.__states = {
            1: self.__wrap_1,
            2: self.__wrap_2,
            3: self.__wrap_3
        }

    def __call__(self, func):
        self.wrapped_func = func

        # if self.flag == 1:
        #     return self.__wrap_1
        # elif self.flag == 2:
        #     return self.__wrap_2
        # elif self.flag == 3:
        #     return self.__wrap_3

        return self.__states.get(self.flag)

    def __wrap_1(self, a, b):
        res = self.__wrapped_func(a, b)
        print(f"{a} + {b} = {res}")
        return res

    def __wrap_2(self, a, b):
        res = self.__wrapped_func(a, b)
        print(res)
        return res

    def __wrap_3(self, a, b):
        res = self.__wrapped_func(a, b)
        print(res)
        return res


@FunctorDecor(3)
def sum(a, b):
    return a + b


sum(1, 1)
sum(1, 2)
sum(4, 2)