
def func_1():
    pass


func_1()


def func_2(a, b):
    pass


func_2(1, 2)


def func_2(a, b=2):
    print(a, b)

#
# func_2(1, 4)
# func_2(1)
#
# func_2(b=3, a=1)


def func_3(args_list=[]):
    for i in args_list:
        print(i)

# func_3()
# func_3([1, 2, 3, 45])


def func_4(a, *args):
    print(type(args))
    print(a)
    print(args)
    pass


# func_4(1)
# func_4(1, 2, 3, 4)


def func_5(**kwargs):
    print(type(kwargs))
    print(kwargs)
    pass


func_5(a=5, b=12)


def func_6(a, b, d=12, *args, **kwargs):
    pass


func_6(1, 2, a=12)


def test(a, b, c):
    pass


# def test_2(*args, **kwargs):
#     args = (1, 2, 3, 4)
#     kwargs = {"a":5, "b":6}
#     test(1, 2, 3, 4, a=5, b=6)
