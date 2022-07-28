# --**Task1**--
from random import randint


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


Exception_list = [ZeroDivisionError, TypeError, RecursionError, StopIteration, OverflowError,
                  IndexError, KeyError, Exception]


@exception_wrapper
def rand_exc_func():
    raise Exception_list[randint(0, 7)]
    return "never give up"


for i in range(10):
    print(rand_exc_func())


# Index does not exist
# Index does not exist
# You have dived too deep into recursion. Always consider the return before diving
# You have dived too deep into recursion. Always consider the return before diving
# Сannot be divided by zero
# Not a valid argument type
# Maybe this key will fit another dict
# Сannot be divided by zero
# Iterator elements are exhausted
# My imagination is exhausted, but the function still throws errors

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


sam_dict = {
    "id": {
        "type": int,
        "required": True,
    },

    "name": {
        "type": str,
        "required": True,
    },
    "age": {
        "type": int,
        "required": False,
    },
    "city": {
        "type": str,
        "required": False,
    }
}
cor_dict = {
    "id": 1,
    "name": "Denys",
    "age": 31,
    "city": "Kyiv"
}
un_cor_dict = {
    "name": 42,
    "city": "Polo Alto"
}

git
@expect
def task2(f_dict: dict):
    d_keys = f_dict.keys()
    res = f'{f_dict["id"]} {f_dict["name"]}'
    if "age" in d_keys:
        res += f'. He is {f_dict["age"]} years old'
    if "city" in d_keys:
        res += f'. And lives in the city of {f_dict["city"]}'
    return res


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
