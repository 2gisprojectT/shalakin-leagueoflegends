__author__ = 'MihaZiK'

from unittest import TestCase
from Lion import MyLion
import unittest


class MyLionTest(TestCase):

    def test_Sit_Antilopa(self):
        l = MyLion("Sit")
        l.meet("Antilopa")

    def test_Goloden_Antilopa(self):
        l = MyLion("Goloden")
        l.meet("Antilopa")

    def test_Sit_Hunter(self):
        l = MyLion("Sit")
        l.meet("Hunter")

    def test_Goloden_Hunter(self):
        l = MyLion("Goloden")
        l.meet("Hunter")

    def test_Sit_Tree(self):
        l = MyLion("Sit")
        l.meet("Tree")

    def test_Goloden_Tree(self):
        l = MyLion("Goloden")
        l.meet("Tree")

    def test_RandomValue(self):
        l = MyLion("Goloden")
        i = 0
        while i < 100:
            l.random()
            i = i+1


if __name__ == '__main__':
    unittest.main()