__author__ = 'MihaZiK'

from unittest import TestCase
from Lion import MyLion
import unittest


class MyLionTest(TestCase):

    def test_Sit_Antilopa(self):
        l = MyLion("Sit")
        l.meet("Antilopa")
        self.assertEqual("Sit", l.state, "Error")

    def test_Goloden_Antilopa(self):
        l = MyLion("Goloden")
        l.meet("Antilopa")
        self.assertEqual("Sit", l.state, "Error")

    def test_Sit_Hunter(self):
        l = MyLion("Sit")
        l.meet("Hunter")
        self.assertEqual("Sit", l.state, "Error")

    def test_Goloden_Hunter(self):
        l = MyLion("Goloden")
        l.meet("Hunter")
        self.assertEqual("Goloden", l.state, "Error")

    def test_Sit_Tree(self):
        l = MyLion("Sit")
        l.meet("Tree")
        self.assertEqual("Goloden", l.state, "Error")

    def test_Goloden_Tree(self):
        l = MyLion("Goloden")
        l.meet("Tree")
        self.assertEqual("Goloden", l.state, "Error")


if __name__ == '__main__':
    unittest.main()
