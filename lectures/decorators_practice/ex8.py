import pytest


@pytest.mark.parametrize(
    ("test_value", "test_value_2"),
    [
        (1, 2),
        (2, 3)
    ]
)
def test_001(test_value, test_value_2):
    pass


from typing import Union


def func(a: Union[int, float]):
    pass