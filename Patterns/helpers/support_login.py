from helpers.base_component import BaseComponent
#-*- coding:UTF-8 -*-

class SupportLogin(BaseComponent):

    selectors = {
        'self': '.credentials',
        'inputLogin': 'user_email',
        'inputPass': 'user_password',
        'commit': 'commit',
    }

    def login(self, login, password):
        self.driver.find_element_by_id(self.selectors['inputLogin']).send_keys(login)
        self.driver.find_element_by_id(self.selectors['inputPass']).send_keys(password)
        self.driver.find_element_by_name(self.selectors['commit']).click()


    def clickLogin(self):
        self.driver.find_element_by_link_text(self.selectors['login']).click()
