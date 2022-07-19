import pytest


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"


@pytest.fixture()
def f_create_user():
    user = User("Misha", "Klimchuk")
    yield user
    del user


def test_full_name(f_create_user):
    user = f_create_user
    assert user.full_name == "Misha Klimchuk"