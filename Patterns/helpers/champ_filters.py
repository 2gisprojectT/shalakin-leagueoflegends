from helpers.base_component import BaseComponent
#-*- coding:UTF-8 -*-


class ChampionsFilter(BaseComponent):

    selectors = {
        'self': 'champion-filter',
        'filter': 'role-fighter',
    }

    def check(self):
        self.driver.find_element_by_id(self.selectors['filter']).click()

