class championsPage():


    def __init__(self, driver):

        self._champ_filter = None
        self._champ_search = None

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

    def open(self):
        self.driver.get("http://gameinfo.ru.leagueoflegends.com/ru/game-info/champions/")