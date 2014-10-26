from helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'submit': '.searchBar__submit._refbook',
        'string': 'suggest__input'
    }

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).clear()
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit']).submit()

    def string(self):
        return self.driver.find_element_by_class_name(self.selectors['string']).get_attribute('value')