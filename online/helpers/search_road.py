__author__ = 'MihaZiK'

from helpers.base_component import BaseComponent


class SearchRoad(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'passage': '.searchBar__tab.searchBar__rsTab',
        'input1': '.searchBar__form .searchBar__textfield._from .suggest__input',
        'input2': '.searchBar__form .searchBar__textfield._to .suggest__input'
    }

    def clickPassage(self):
        self.driver.find_element_by_css_selector(self.selectors['passage']).click()

    def inputRoads(self, input1, input2):
        self.driver.find_element_by_css_selector(self.selectors['input1']).send_keys(input1)
        self.driver.find_element_by_css_selector(self.selectors['input2']).send_keys(input2)
