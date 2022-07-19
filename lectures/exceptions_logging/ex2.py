

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except TypeError:
        return div(int(a), int(b))
    except Exception:
        print("ERROR")


# print(div(1, 0))
# print(div("1", 2))

def get_element(collection, param):
    try:
        return collection[param]
    except (IndexError, KeyError) as exception:
        print("NotFound", exception.args[0])

# get_element([1, 2], 45)
# get_element({1:"a"}, 45)


class MyException1(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message


try:
    raise MyException1("message123123123123")
except MyException1 as ex:
    pass