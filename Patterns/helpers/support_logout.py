from helpers.base_component import BaseComponent
#-*- coding:UTF-8 -*-



class SupportLogout(BaseComponent):

    selectors = {
        'self': '.home.home-index',
        'out': u'выход',

    }

    def logout(self):
        self.driver.find_element_by_link_text(self.selectors['out']).click()

