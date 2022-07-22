import pytest

from calc.calc import Calc


def test_sum_001():
    assert Calc.sum(1, 2, 3, 4) == 10


def test_sum_002():
    with pytest.raises(TypeError):
        assert Calc.sum("1")

