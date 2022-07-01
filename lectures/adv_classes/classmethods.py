#
# class User:
#     version = 1
#
#     def __init__(self):
#         self.name = "Misha"
#
#     def get_phone(self):
#         return "123213123"
#
#     @classmethod
#     def test(cls):
#         pass
#
#     @classmethod
#     def get_user_version(cls):
#         # return User.version
#         return cls.test()
#
#     def test_2(self):
#         self.get_user_version()
#
# pass
# user = User()
#
# user.get_phone()
# User.get_phone(user)
#
# User.get_user_version()


class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    @classmethod
    def create_user_from_dict(cls, user_dict: dict):
        return cls(name=user_dict.get("Name"), age=user_dict.get("Age"), city=user_dict.get("City"))


user = User("Misha", 25, "Kyiv")

user_dict = {
    "NAME": "Misha",
    "Age": 33,
    "City": "Kyiv",
    "Phone": "2434123"
}

user_1 = User.create_user_from_dict(user_dict)

