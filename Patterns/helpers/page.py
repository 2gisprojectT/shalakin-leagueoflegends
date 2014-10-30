class Page():
    def __init__(self, driver):

        self.driver = driver
        self._support = None
        self._sup_search_bar = None
        self._sup_login = None
        self._sup_logout = None
        self._champions = None
        self._champ_filter = None
        self._champ_search = None

    def support(self):
        from helpers.support import Support

        if self._support is None:
            self._support = Support(self.driver, self.driver.find_element_by_css_selector(Support.selectors['self']))
        return self._support

    def sup_search_bar(self):
        from helpers.support_search_bar import SupSearchBar

        if self._sup_search_bar is None:
            self._sup_search_bar = SupSearchBar(self.driver, self.driver.find_element_by_css_selector(SupSearchBar.selectors['self']))
        return self._sup_search_bar

    def sup_login(self):
        from helpers.support_login import SupportLogin

        if self._sup_login is None:
            self._sup_login = SupportLogin(self.driver, self.driver.find_element_by_css_selector(SupportLogin.selectors['self']))
        return self._sup_login

    def sup_logout(self):
        from helpers.support_logout import SupportLogout

        if self._sup_logout is None:
            self._sup_logout = SupportLogout(self.driver, self.driver.find_element_by_css_selector(SupportLogout.selectors['self']))
        return self._sup_logout

    def champions(self):
        from helpers.champions import Champions

        if self._champions is None:
            self._champions = Champions(self.driver, self.driver.find_element_by_id(Champions.selectors['self']))
        return self._champions

    def champ_filter(self):
        from helpers.champ_filters import ChampionsFilter

        if self._champ_filter is None:
            self._champ_filter = ChampionsFilter(self.driver, self.driver.find_element_by_id(ChampionsFilter.selectors['self']))
        return self._champ_filter

    def champ_search(self):
        from helpers.champ_search import ChampionsSearch

        if self._champ_search is None:
            self._champ_search = ChampionsSearch(self.driver, self.driver.find_element_by_class_name(ChampionsSearch.selectors['self']))
        return self._champ_search

    def open(self, url):
        self.driver.get(url)
