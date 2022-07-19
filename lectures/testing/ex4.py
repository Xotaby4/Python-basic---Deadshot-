from unittest import TestCase


def div(a, b) -> float:
    return a / b


def sum(a, b):
    return a + b


class TestDiv(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("SET UP")

    def tearDown(self) -> None:
        print("tearDown")

    def test_001(self):
        res = div(4, 2)
        self.assertEqual(res, 2)

    def test_002(self):
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)


class TestSum(TestCase):
    pass
