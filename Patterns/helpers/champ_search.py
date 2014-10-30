from helpers.base_component import BaseComponent
#-*- coding:UTF-8 -*-


class ChampionsSearch(BaseComponent):

    selectors = {
        'self': 'btn-input',
        'input': 'filter-name',
    }

    def search(self, query):
        self.driver.find_element_by_id(self.selectors['input']).clear()
        self.driver.find_element_by_id(self.selectors['input']).send_keys(query)
