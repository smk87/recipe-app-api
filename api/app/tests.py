from django.test import TestCase
from app.calc import add, sub


class CalcTest(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub_numbers(self):
        self.assertEqual(sub(9, 4), 55)
