
def expect(model):
    def big_wrap(func):
        def wrap(data):
            print("start expect")
            res = func(data)
            print("end expect")
            return res
        return wrap
    return big_wrap


def marshal(model):
    def big_wrap(func):
        def wrap(*args, **kwargs):
            print("start marshal")
            raise Exception()
            res = func(*args, **kwargs)
            print("end marshal")
            return res
        return wrap
    return big_wrap


def exception_wrapper(func):
    def wrap(*args, **kwargs):
        print("start exception_wrapper")
        res = None
        try:
            res = func(*args, **kwargs)
        except Exception:
            pass
        print("end exception_wrapper")
        return res
    return wrap


@exception_wrapper
@expect({})
@marshal({})
def func_1(data):
    pass


@exception_wrapper
def func_2():
    pass


func_1({})


