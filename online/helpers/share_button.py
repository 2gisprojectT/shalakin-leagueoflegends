__author__ = 'MihaZiK'

from helpers.base_component import BaseComponent


class ShareButton(BaseComponent):

    selectors = {
        'self': '.extras__group',
        'input': '.share__popupUrlInput',
        'share': '.extras__btn.extras__share'
    }

    def getLink(self):
        return self.driver.find_element_by_css_selector(self.selectors['input']).get_attribute('value')

    def clickShare(self):
        self.driver.find_element_by_css_selector(self.selectors['share']).click()
