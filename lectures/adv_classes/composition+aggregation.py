#
#
# class Page:
#     def __init__(self, num):
#         self.num = num
#
#
# class Album:
#     def __init__(self, pages_num):
#         self.pages = []
#         for num in range(pages_num):
#             self.pages.append(Page(num))
#
#
# album_1 = Album(10)
# pass
#


# class Engine:
#     pass
#
#
# class Car:
#     def __init__(self, engine: Engine):
#         self.engine = engine
#
# en = Engine()
#
# car = Car(en)
# pass

class Address:
    def __init__(self, str_, post_code, number):
        self.str = str_
        self.number = number
        self.post_code = post_code
        self.users = []


class User:
    def __init__(self, address):
        self.address = address


address = Address("Var", 2, 20222)

user_1 = User(address)
user_2 = User(address)


class Engine:
    def __init__(self, car=None):
        self.car = car


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.engine.car = self

en = Engine()

car = Car(en)
pass