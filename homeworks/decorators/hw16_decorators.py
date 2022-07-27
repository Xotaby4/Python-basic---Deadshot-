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


def expect(sam_dict: dict):
    def big_wrap(func):
        def wrap(f_dict: dict):
            f_key = f_dict.keys()
            for key, value in sam_dict:
                if value.required:
                    try:
                        if value['type'] == type(f_key[key]):
                            continue
                        else:
                            raise ValidationError
                    except KeyError:
                        raise ValidationError
            return func(f_dict)

        return wrap

    return big_wrap


# --**Task3**--
def expect(sam_dict: dict):
    def big_wrap(func):
        def wrap(*args, **kwargs):
            f_dict = func(*args, **kwargs)
            f_key = f_dict.keys()
            for key, value in sam_dict:
                if value.required:
                    try:
                        if value['type'] == type(f_key[key]):
                            continue
                        else:
                            raise ValidationError
                    except KeyError:
                        raise ValidationError
            return f_dict

        return wrap

    return big_wrap
