from unittest import TestCase
from VacuumCleaner import VacuumCleaner

'''
1. повне прибирання на яке вистачає ресурсів
2. прибирання без вологого прибирання на яке вистачає ресурсів
3. прибирання під час якого не вистачило заряду батареї (перевірити що start_cleaning повернула False і що заряд батареї 0%)
4. прибирання під час якого заповнився сміттє бак (перевірити що start_cleaning повернула False і що сміттєбак повний)
5. прибирання під час якого не вистачило води (перевірити що start_cleaning повернула False і що бак з водою пустий)
6. проперті info повертає правильне значення
'''


class TestVacuumCleaner(TestCase):

    def setUp(self) -> None:
        self.test_cleaner = VacuumCleaner(0, 500, 100, "test_series")
        print(self.test_cleaner.info)

    def tearDown(self) -> None:
        self.est_cleaner = None

    def test_full_cleaning(self):
        self.assertTrue(self.test_cleaner.start_cleaning(True, 20))

    def test_dry_cleaning(self):
        self.assertTrue(self.test_cleaner.start_cleaning(False, 20))

    def test_battery_low(self):
        self.test_cleaner.q_battery = 20
        self.assertFalse(self.test_cleaner.start_cleaning(False, 25))
        self.assertEqual(self.test_cleaner.q_battery, 0)

    def test_full_dust(self):
        self.test_cleaner.f_garbage = self.test_cleaner.v_garbage - 100
        self.assertFalse(self.test_cleaner.start_cleaning(False, 25))
        self.assertEqual(self.test_cleaner.f_garbage, self.test_cleaner.v_garbage)

    def test_no_water(self):
        self.test_cleaner.f_water = 50
        self.assertFalse(self.test_cleaner.start_cleaning(True, 25))
        self.assertEqual(self.test_cleaner.f_water, 0)

    def test_info(self):
        info = "test_series; power - 100%; water tank - 100%; trash tank - 0%"
        self.assertEqual(self.test_cleaner.info, info)
