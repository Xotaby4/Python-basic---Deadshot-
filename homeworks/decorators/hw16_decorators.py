# --**Task1**--

def exception_wrapper(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Сannot be divided by zero"
        except TypeError:
            return "Not a valid argument type"
        except RecursionError:
            return "You have dived too deep into recursion. Always consider the return before diving"
        except StopIteration:
            return "Iterator elements are exhausted"
        except OverflowError:
            return "Result too large to display"
        except IndexError:
            return "Index does not exist"
        except KeyError:
            return "Maybe this key will fit another dict"
        except Exception:
            return "My imagination is exhausted, but the function still throws errors"

    return wrap


# @exception_wrapper
def som_func(a, b):
    return som_func(a / b, b)


print(som_func(1, 2))

# --**Task2**--

class ValidationError(Exception):
    pass

def expect(sampl_dict: dict):
    def big_wrap
    pass

# --**Task3**--