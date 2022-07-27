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
    pass
