
class MyClass:
    def __init__(self):
        self._temperature = 12

    @property
    def temperature(self):
        return self._temperature * 1.2

    @temperature.setter
    def temperature(self, value):
        self._temperature = value / 1.2

    def recalc(self):
        self._temperature += 1


obj = MyClass()
obj.temperature = 123
setattr(obj, "temperature", 123)

class User:
    def __init__(self):
        self.name = "M"
        self.surname = "K"

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def set_surname(self, name=None, surname=None):
        if name:
            self.name = name

        if surname:
            self.surname = surname


obj = MyClass()
