#-*- coding:UTF-8 -*-
from helpers.base_component import BaseComponent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SupSearchBar(BaseComponent):

    selectors = {
        'self': '.content.content_green',
        'input': 'suggestions_query',
        'submit': 'suggestion_submit',
    }

    def search(self, query):
        """
        Другим способом категорически отказывается искать хоть что либо, перебрал все варианты, через find_element ничего найти не может
        """
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.selectors['input']))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.selectors['input']))).send_keys(query)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.selectors['submit']))).submit()
        """
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_id(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()
        """
