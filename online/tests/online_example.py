#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page

class SeleniumTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.page = Page(cls.driver)
        cls.page.open("http://2gis.ru")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    """
    def test_share(self):
        #self.driver.implicitly_wait(10)
        self.page.search_bar().search(u'кафе')
        self.page.share_button().clickShare()
        share_link = self.page.share_button().getLink()
        self.page.open(share_link)
        self.assertEqual(self.page.search_bar().string(), u'кафе')
    """
    def test_search_road(self):
        self.page.search_road().clickPassage()
        self.page.search_road().inputRoads(u'Золотая нива', u'Студенческая')
        time = self.page.search_road_result().getTime()
        self.assertIsNone(time)




if __name__ == '__main__':
    unittest.main()
