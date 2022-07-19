import pytest


def div(a, b) -> float:
    return a / b

VERSION = 1.0


class TestDiv:
    @pytest.mark.parametrize(
        ("a", "b", "c"), [
            (1, 1, 1),
            (2, 1, 2),
            (4, 2, 2),
            (100, 10, 10),
        ]
    )
    @pytest.mark.skipif(VERSION != 2.0, reason="wrong version")
    def test_div_001(self, a, b, c):
        assert div(a, b) == c

    def test_div_002(self):
        with pytest.raises(ZeroDivisionError):
            div(1, 0)
