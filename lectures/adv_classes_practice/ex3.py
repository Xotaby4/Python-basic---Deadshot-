

class MyClass:
    value = 10  # class attr

    def __init__(self):
        self.name = "Misha"

    def get_name(self):
        MyClass.get_value()
        self.get_value()
        return self.name

    @classmethod
    def get_value(cls):
        return cls.value

    @staticmethod
    def func():
        MyClass.get_value()
        MyClass.value


# print(MyClass.value)
# print(MyClass.name)
obj_1 = MyClass()
obj_2 = MyClass()
pass
obj_3 = MyClass()

# print(obj_1.value)
# print(obj_1.name)