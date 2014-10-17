__author__ = 'MihaZiK'
#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginLoL(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://ru.leagueoflegends.com/"

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)

        support = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, u"ПОДДЕРЖКА"))
        )
        support.click()

        enter = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, u"вход"))
        )
        enter.click()

        email = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "user_email"))
        )
        email.clear()
        email.send_keys("deathtotti@yandex.ru")

        password = driver.find_element_by_id("user_password")
        password.clear()
        password.send_keys("rcthjy")

        login = driver.find_element_by_name("commit")
        login.click()

        self.assertEqual(u"Михаил", driver.find_element_by_id("top-right-name").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()