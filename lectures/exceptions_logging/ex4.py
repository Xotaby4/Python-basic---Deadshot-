import timeit


def func():
    a = 1
    b = 1
    if a == 0:
        pass
    else:
        b / a


def func_2():
    try:
        a = 1
        b = 1
        b / a
    except ZeroDivisionError:
        pass


print(timeit.repeat(func))
print(timeit.repeat(func_2))