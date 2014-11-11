class supportPage():


    def __init__(self, driver):

        self.driver = driver
        self._support = None
        self._sup_search_bar = None
        self._sup_login = None
        self._sup_logout = None

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

    def open(self):
        self.driver.get("https://support.riotgames.com/hc/ru")
