import pytest

from users.user import User


@pytest.fixture()
def get_user():
    yield User("Misha", "KL")


@pytest.fixture()
def user_helper():
    class UserHelper:
        @classmethod
        def create_user(cls, *args):
            user = User(*args)
            return user

        def get_users_parent_child(self, user_1_data, user_2_data):
            user_1 = self.create_user(user_1_data["name"], user_1_data["surname"])
            user_2 = self.create_user(user_2_data["name"], user_2_data["surname"])
            user_1.set_parent(user_2)
            return user_1, user_2

    helper_obj = UserHelper()
    yield helper_obj


@pytest.mark.parametrize(
    ("name", "surname"), (
        ["Misha", "KL"],
        ["Oleg", "LR"]
    )
)
def test_user_full_name(name, surname, user_helper):
    user = user_helper.create_user(name, surname)
    assert user.full_name == f"{name} {surname}"


@pytest.mark.parametrize(
    ("user_1_data", "user_2_data"), (
        [
            {
                "name": "Misha",
                "surname": "KL",
            },
            {
                "name": "Oleg",
                "surname": "LR",
            }
        ],
        [
            {
                "name": "Misha1111",
                "surname": "1KL",
            },
            {
                "name": "Oleg23123",
                "surname": "L2R",
            }
        ]
    )
)
def test_users(user_1_data, user_2_data, user_helper):
    user_1, user_2 = user_helper.get_users_parent_child(user_1_data, user_2_data)

    assert user_1.parent is user_2
    assert user_1 in user_2.child
