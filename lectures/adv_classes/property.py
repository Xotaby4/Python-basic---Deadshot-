# property

class User:
    def __init__(self, name, surname, card_number):
        self.name = name
        self.surname = surname
        self.__card_number = card_number

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @property
    def card_number(self):
        return f"{'*' * 12 }{self.__card_number[-4:]}"

    @card_number.setter
    def card_number(self, value):
        self.__card_number = value

    @card_number.deleter
    def card_number(self):
        pass


user = User("Misha", "Klimchuk", "1234123412341234")

print(user.fullname)
user.card_number = "4321432143214321"
del user.card_number

fullname = "Misha Klimchuk"

name, surname = fullname.split(" ")
pass


class User1:
    def __init__(self, name, surname, card_number):
        self.name = name
        self.surname = surname
        self.__card_number = card_number

    def set_card_number(self, value):
        self.__card_number = value

    card_number = property(fset=set_card_number)


user1 = User1("Misha", "Klimchuk", "1234123412341234")
user1.__card_number
