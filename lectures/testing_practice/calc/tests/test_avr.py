import pytest

from calc.calc import Calc


@pytest.mark.parametrize(
    ("values", "res"), (
        [[1, 1, 1, 1], 1],
        [[2, 8], 5],
    )
)
def test_avg_001(values, res):
    assert Calc.avg(*values) == res


@pytest.mark.parametrize(
    "values", (
        ("1", 1, 2),
        {"1", 2},
        ["4"],
        frozenset("1")
    )

)
def test_avg_002(values):
    with pytest.raises(TypeError):
        assert Calc.avg(*values)
