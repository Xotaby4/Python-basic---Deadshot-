
class My1:
    pass


class My2:
    pass


class MyClass(My1):
    value = 10
    def func(self):
        print("!!!!")


class MyClass2(My2):
    value = 20
    def func(self):
        print("333")


class NewClass(MyClass, MyClass2):
    value = 30

    def func(self):
        print(super(MyClass, self).value)


obj = NewClass()
obj.func()