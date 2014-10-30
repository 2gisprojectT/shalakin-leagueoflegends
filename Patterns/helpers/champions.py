from helpers.base_component import BaseComponent
#-*- coding:UTF-8 -*-
from helpers.page import Page

class Champions(BaseComponent):

    selectors = {
        'self': 'main-navigation',
        'champs': 'http://gameinfo.ru.leagueoflegends.com/ru/game-info/champions/',
    }

    def open(self):
        self.page = Page(self.driver)
        self.page.open(self.selectors['champs'])
