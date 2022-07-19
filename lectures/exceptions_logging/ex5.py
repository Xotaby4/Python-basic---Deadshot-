

def func_1():
    raise TypeError


def func_2():
    try:
        func_1()
    except TypeError as ex:
        print("TypeError")
        raise ex


def func():
    try:
        func_2()
    except Exception as ex:
        print("EXCEPTION")


func()