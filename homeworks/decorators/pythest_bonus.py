import pytest
import hw16_decorators as hw
from random import randint


@pytest.fixture()
def f_task1():
    pass


@pytest.fixture()
def f_task2():
    pass


def test_exception_wrapper():
    for i in range(100):
        assert (hw.rand_exc_func in hw.Exception_list) == False, "Something unexpected happened"


def test_expect():
    assert hw.task2(hw.cor_dict) == "1 Denys. He is 31 years old. And lives in the city of Kyiv"
    with pytest.raises(hw.ValidationError):
        hw.task2(hw.un_cor_dict)


def test_marshal():
    assert hw.task3(1, "Denys", 31, "Kyiv") == hw.cor_dict
    with pytest.raises(hw.ValidationError):
        hw.task3("1", 42)
