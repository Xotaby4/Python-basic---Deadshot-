from unittest import TestCase


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"


class TestUser(TestCase):

    def setUp(self) -> None:
        self.user = User("Misha", "Klimchuk")

    def tearDown(self) -> None:
        self.user = None

    def test_001(self):
        self.assertEqual(self.user.full_name, "Misha Klimchuk")
