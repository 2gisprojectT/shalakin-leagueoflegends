#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page


class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.page = Page(self.driver)
        self.page.open("http://ru.leagueoflegends.com/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    #Поиск статей
    def test_search_support(self):
        self.page.support().clickSupport()
        self.page.sup_search_bar().search('Ranked')
        self.assertEqual(u"Командные ранговые игры - первые шаги", self.driver.find_element_by_link_text(u'Командные ранговые игры - первые шаги').text)
    #Тест авторизации
    def test_login_support(self):
        self.page.support().clickSupport()
        self.page.support().clickLogin()
        self.page.sup_login().login('deathtotti@yandex.ru', '******')
        self.assertEqual(u"Михаил", self.driver.find_element_by_id("top-right-name").text)
    #Тест разлогинивания
    def test_logout_support(self):
        self.page.support().clickSupport()
        self.page.support().clickLogin()
        self.page.sup_login().login('deathtotti@yandex.ru', '******')
        self.page.sup_logout().logout()
        self.assertEqual(u"Вы завершили сеанс работы.", self.driver.find_element_by_id("notice").text)
    #Тест фильтра чемпионов
    def test_champions_filter(self):
        self.page.champions().open()
        self.page.champ_filter().check()
        self.assertEqual(u"Атрокс", self.driver.find_element_by_link_text(u'Атрокс').text)
    #Тест поиска чемпионов
    def test_champions_search(self):
        self.page.champions().open()
        self.page.champ_search().search(u'Ву')
        self.assertEqual(u"Вуконг", self.driver.find_element_by_link_text(u'Вуконг').text)

if __name__ == '__main__':
    unittest.main()
