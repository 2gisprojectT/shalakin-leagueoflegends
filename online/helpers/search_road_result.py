__author__ = 'MihaZiK'

from helpers.base_component import BaseComponent

class searchRoadResult(BaseComponent):

    selectors = {
        'self': '.online__panels',
        'time': '.routeResults__routeHeader .routeResults__routeHeaderWrap .routeResults__time',
    }

    def getTime(self):
        return self.driver.find_element_by_css_selector(self.selectors['time']).text