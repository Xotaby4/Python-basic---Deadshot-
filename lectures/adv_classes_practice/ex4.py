

class MyClass1:
    @classmethod
    def func(cls):
        print("func MyClass1")

    @classmethod
    def func_2(cls):
        cls.func()


class MyClass2(MyClass1):
    @classmethod
    def func(cls):
        print("func MyClass2")


MyClass2.func_2()
