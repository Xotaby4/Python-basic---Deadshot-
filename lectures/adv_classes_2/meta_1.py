from collections import namedtuple

# User = namedtuple("User", ("name", "age"))
# user = User("Misha", 12)

# def func(self, name):
#     self.name = name
#
# User = type("User", (), {"version": 1, "__init__": func})
#
# user = User("Misha")
# pass

# class User:
#     def __init__(self, name):
#         self.name = name


class UpperAttrMetaclass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        uppercase_attr = {}
        for name, value in future_class_attr.items():
            if name.startswith('__'):
                continue
            uppercase_attr[f"{name}_API"] = value
        return type(future_class_name, future_class_parents, uppercase_attr)


class Foo(metaclass=UpperAttrMetaclass):
    bar = 'bip'


obj = Foo()
pass