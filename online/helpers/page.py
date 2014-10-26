class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None
        self._search_result = None
        self._share_button = None
        self._search_road = None
        self._search_road_result = None

    def search_bar(self):
        from helpers.search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_css_selector(SearchBar.selectors['self']))
        return self._search_bar

    def search_result(self):
        from helpers.search_result import SearchResult

        if self._search_result is None:
            self._search_result = SearchResult(self.driver, self.driver.find_element_by_css_selector(SearchResult.selectors['self']))
        return self._search_result

    def share_button(self):
        from helpers.share_button import ShareButton

        if self._share_button is None:
            self._share_button = ShareButton(self.driver, self.driver.find_element_by_css_selector(ShareButton.selectors['self']))
        return self._share_button

    def search_road(self):
        from helpers.search_road import SearchRoad

        if self._search_road is None:
            self._search_road = SearchRoad(self.driver, self.driver.find_element_by_css_selector(SearchRoad.selectors['self']))
        return self._search_road

    def search_road_result(self):
        from helpers.search_road_result import searchRoadResult

        if self._search_road_result is None:
            self._search_road_result = searchRoadResult(self.driver, self.driver.find_element_by_css_selector(searchRoadResult.selectors['self']))
        return self._search_road_result

    def open(self, url):
        self.driver.get(url)

