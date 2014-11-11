from helpers.base_component import BaseComponent
#-*- coding:UTF-8 -*-

class Support(BaseComponent):

    selectors = {
        'self': '.pvpnet-bar-support-link',
        'login': u'вход',
    }

    def clickLogin(self):
        self.driver.find_element_by_link_text(self.selectors['login']).click()

