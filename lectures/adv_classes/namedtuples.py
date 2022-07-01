from collections import namedtuple
dict_ = {
    "User": ("name", "age", "city"),
    "Car": ("name", "year")
}

User = namedtuple("User", ("name", "age", "city"))
user = User(name="M", age=22, city="sds")
pass
