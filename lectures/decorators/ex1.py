from random import randint


def f_1(a, b):
    print("cb1")
    return a + b


def f_2():
    return "HI"


new_name_func = f_2
pass

def func(cb_1, cb_2):
    if randint(0, 2) == 1:
        cb_1()
    else:
        cb_2()


def func_2():
    return f_1


# result = func_2()
# print(result)
# print(result(1, 2))


# lambda_func = lambda a, b: a+b
# pass

def big_func():
    print("i am big_func")
    a = 5
    def little_func():
        print("i am little_func")
        pass
    little_func()

# big_func()


def test_f():
    a = 5
    def test_2_f():
        print(a)
    return test_2_f


result = test_f()
result()
result()
result()
result()
result()
