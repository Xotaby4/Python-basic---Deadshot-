

def func_1(self):
    print(1)


def func_2(self):
    print(2)


def func_3(param):
    attrs = {}
    if param == 1:
        attrs["name"] = func_1
        attrs["surname"] = func_2
    if param == 2:
        attrs["surname"] = func_2

    return type("MyClass", (), attrs)


class MyClass:
    def name(self):
        print(1)

    def surname(self):
        print(2)


class MyClassBase:
    def surname(self):
        print(2)

class MyClass(MyClassBase):
    def name(self):
        print(1)


def func_4(param):
    if param == 1:
        return MyClass
    if param == 2:
        return MyClassBase


