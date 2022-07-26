
def decorator_print_result_v5(print_pattern):
    def big_wrap(func):
        def wrap(a, b):
            res = func(a, b)
            print(print_pattern.format(res))
            return res
        return wrap
    return big_wrap


@decorator_print_result_v5("result is {}")
def func_1(a, b):
    return a + b


@decorator_print_result_v5("res = {}")
def func_2(a, b):
    return a - b

# big_wrap_func_1 = decorator_print_result_v5("result is {}")
# wrap_func_1 = big_wrap_func_1(func_1)
# wrap_func_1(1, 2)
# wrap_func_1(2, 2)
# wrap_func_1(2, 2)
#
# big_wrap_func_2 = decorator_print_result_v5("res = {}")
# wrap_func_2 = big_wrap_func_2(func_2)
# wrap_func_2(1, 2)
# wrap_func_2(2, 2)
# wrap_func_2(2, 2)


func_1(1, 2)
func_1(2, 2)
func_1(3, 2)
func_1(4, 2)


func_2(1, 2)
func_2(2, 2)
func_2(3, 2)
func_2(4, 2)

