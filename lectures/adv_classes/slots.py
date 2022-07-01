import timeit
import statistics


class MyClassSlot:
    __slots__ = ("name", )


class MyClass:
    pass


def set_get_delete(obj):
    obj.name = 12
    obj.name
    del obj.name


def test_slot():
    set_get_delete(MyClassSlot())


def test_no_slot():
    set_get_delete(MyClass())


print(statistics.mean(timeit.repeat(test_slot)))
print(statistics.mean(timeit.repeat(test_no_slot)))
