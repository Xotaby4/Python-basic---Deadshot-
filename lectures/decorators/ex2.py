

def decorator_print_result_v1():
    res = func_1(1, 2)
    print(f"1 + 2 = {res}")
    return res


def decorator_print_result_v2(a, b):
    res = func_1(a, b)
    print(res)
    return res

def decorator_print_result_v3(a, b, func):
    res = func(a, b)
    print(res)
    return res


def func_1(a, b):
    return a + b


def func_2(a, b):
    return a - b

# func(1, 2)
# decorator_print_result_v1()
# decorator_print_result_v2(1, 2)
#
# decorator_print_result_v3(1, 2, func_1)
# decorator_print_result_v3(1, 2, func_2)


def decorator_print_result_v4(func):
    def wrap(a, b):
        res = func(a, b)
        print(f"{res}")
        return res
    return wrap


# wraped_func_1 = decorator_print_result_v4(func_1)
#
# wraped_func_1(1, 2)
# wraped_func_1(2, 2)
# wraped_func_1(3, 2)
#
# wraped_func_2 = decorator_print_result_v4(func_2)
#
# wraped_func_2(1, 2)
# wraped_func_2(2, 2)
# wraped_func_2(3, 2)


@decorator_print_result_v4
def func_1(a, b):
    return a + b


func_1(1, 2)
func_1(2, 2)
func_1(3, 2)
func_1(4, 2)

@decorator_print_result_v4
def func_2(a, b):
    return a - b

func_2(1, 2)
func_2(2, 2)
func_2(3, 2)
func_2(4, 2)