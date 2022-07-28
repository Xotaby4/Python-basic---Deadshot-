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


def validator(s_dict: dict, f_dict: dict) -> None:
    for key, value in s_dict.items():
        if value["required"]:
            try:
                if value["type"] == type(f_dict[key]):
                    continue
                else:
                    raise ValidationError
            except KeyError:
                raise ValidationError


def expect(s_dict: dict):
    def big_wrap(func):
        def wrap(f_dict: dict):
            f_key = f_dict.keys()
            validator(s_dict, f_dict)
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


@expect(sam_dict)
def task2(f_dict: dict) -> str:
    d_keys = f_dict.keys()
    res = f'{f_dict["id"]} {f_dict["name"]}'
    if "age" in d_keys:
        res += f'. He is {f_dict["age"]} years old'
    if "city" in d_keys:
        res += f'. And lives in the city of {f_dict["city"]}'
    return res


print(task2(cor_dict))


# 1 Denys. He is 31 years old. And lives in the city of Kyiv


# --**Task3**--
def marshal(s_dict: dict):
    def big_wrap(func):
        def wrap(*args, **kwargs):
            f_dict = func(*args, **kwargs)
            f_key = f_dict.keys()
            validator(s_dict, f_dict)
            return f_dict

        return wrap

    return big_wrap


@marshal(sam_dict)
def task3(id_, name, age=None, city=None):
    res = {"id": id_, "name": name}
    if age:
        res["age"] = age
    if "name":
        res["city"] = city
    return res


dry = task3(1, "Denys", 31, "Kyiv")
print(dry, dry == cor_dict)
