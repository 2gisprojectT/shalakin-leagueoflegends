__author__ = 'MihaZiK'
#-*- coding:UTF-8 -*-
from unittest import TestCase
from unittest_data_provider import data_provider
from selenium import webdriver
from helpers.page import Page
import unittest

class dataProviderTest(TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://2gis.ru")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    data = lambda: (
        (u'Кафе', True),
        (u'Клуб', True),
        (u'Компьютер', True),
        ('dsfafSDSFFASFAHSHJADgn', False),
        ('wvvdwqqrwsdg442', False),
        ('dxbvbwer1233', False)
    )

    @data_provider(data)
    def test_search(self, string, result):
        self.page.search_bar().search(string)
        self.assertEqual(self.page.search_result.count > 0, result, 'Wrong count of firms')

if __name__ == '__main__':
    unittest.main()