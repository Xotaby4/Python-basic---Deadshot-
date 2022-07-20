import pytest
from VacuumCleaner import VacuumCleaner
import VacuumCleanerExeption

'''
1. повне прибирання на яке вистачає ресурсів
2. прибирання без вологого прибирання на яке вистачає ресурсів
3. прибирання під час якого не вистачило заряду батареї (перевірити що start_cleaning повернула False і що заряд батареї 0%)
4. прибирання під час якого заповнився сміттє бак (перевірити що start_cleaning повернула False і що сміттєбак повний)
5. прибирання під час якого не вистачило води (перевірити що start_cleaning повернула False і що бак з водою пустий)
6. проперті info повертає правильне значення
'''


@pytest.fixture()
def f_test_cleaner():
    test_cleaner = VacuumCleaner(0, 500, 100, "test_series")
    yield test_cleaner
    del test_cleaner


def test_full_cleaning(f_test_cleaner):
    assert (f_test_cleaner.start_cleaning(True, 20) == True), "False != True"


def test_dry_cleaning(f_test_cleaner):
    assert (f_test_cleaner.start_cleaning(False, 20) == True), "False != True"


def test_battery_low(f_test_cleaner):
    f_test_cleaner.q_battery = 20
    assert (f_test_cleaner.start_cleaning(False, 25) == False), "True != False"
    assert (f_test_cleaner.q_battery == 0), f"{f_test_cleaner.q_battery} != 0"


def test_full_dust(f_test_cleaner):
    f_test_cleaner.f_garbage = f_test_cleaner.v_garbage - 100
    assert (f_test_cleaner.start_cleaning(False, 25) == False), "True != False"
    assert (f_test_cleaner.f_garbage == f_test_cleaner.v_garbage)


def test_no_water(f_test_cleaner):
    f_test_cleaner.f_water = 50
    assert (f_test_cleaner.start_cleaning(True, 25) == False), "False != True"
    assert (f_test_cleaner.f_water == 0), f"{f_test_cleaner.f_water} != 0"


def test_info(f_test_cleaner):
    info = "test_series; power - 100%; water tank - 100%; trash tank - 0%"
    assert (f_test_cleaner.info == info), f"{f_test_cleaner.info} != {info}"


# Bonus
@pytest.fixture
def exhausted():
    exhausted_cleaner = VacuumCleaner(1200, 0, 0, "exhausted")
    yield exhausted_cleaner
    del exhausted_cleaner


def test_add_trash(exhausted):
    with pytest.raises(VacuumCleanerExeption.FullTrashTank):
        exhausted.add_trash()


def test_wet_cleaning(exhausted):
    with pytest.raises(VacuumCleanerExeption.EmptyWatterTank):
        exhausted.wet_cleaning()


def test_battery_drain(exhausted):
    with pytest.raises(VacuumCleanerExeption.LowBattery):
        exhausted.battery_drain()
