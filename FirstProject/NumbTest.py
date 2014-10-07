__author__ = 'MihaZiK'

from unittest import TestCase
from First import Numbers
import unittest


class NumbersTest(TestCase):
    def test_init(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(1, num.a, 'A have wrong value')
        self.assertEqual(2, num.b, 'B have wrong value')
        self.assertEqual(3, num.c, 'C have wrong value')

    def test_init(self):
        num = Numbers(1, 2, -3)
        self.assertEqual(0, num.c, 'C<0')

    def test_sum(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(6, num.sum(), 'Error')

    def test_multiplication(self):
        num = Numbers(0, 2, 3)
        self.assertEqual(0, num.multiplication(), 'Error')

    def test_abs_multiplication(self):
        num = Numbers(1, 2, 3)
        self.assertEqual(6, num.abs_multiplication(), 'Error')


if __name__ == '__main__':
    unittest.main()