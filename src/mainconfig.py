from configparser import ConfigParser
from .sorter import SortRule, SortOrder as sord
from .book import BookAttributes as ba

from os import path

class InvalidConfigFile(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class InvalidConfigAttr(Exception):

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class MainConfig():

    SORTER_CONFIG = 'SorterConfig'
    RULES = 'Rules'
    LOAD_INI = 'BooksINI'
    SAVE_INI = 'SaveINI'

    MANDATORY_SECTIONS = [SORTER_CONFIG, RULES]
    MANDATORY_CONFIGS = [LOAD_INI, SAVE_INI]

    def __init__(self, config_file):
        from .booksconfig import BooksConfig
        
        self.config_file = config_file
        self.mainConfig = ConfigParser()
        
        self.loadINI = None
        self.saveINI = None
        self.rulesList = None

        self.configure()
        self.bkconf = BooksConfig(self.loadINI)

    def save_books(self, books):
        save = ConfigParser()
        for book in books:
            save[book.title] = {}
            savebook = save[book.title]
            savebook[ba.author.value] = book.author
            savebook[ba.edition_year.value] = book.edition_year
        with open(self.saveINI, 'w') as savefile:
            save.write(savefile)

    def get_rules(self):
        return list(self.rulesList)

    def get_books(self):
        return self.bkconf.get_books()

    def is_valid_config(self):
        if self.mainConfig.sections() == self.MANDATORY_SECTIONS:
            for element in self.MANDATORY_CONFIGS:
                if not element in self.mainConfig[self.SORTER_CONFIG]:
                    return False
            return True
        return False

    def init_INIs(self):
        res = self.mainConfig[self.SORTER_CONFIG][self.LOAD_INI]
        if res:
            self.loadINI = res
        res = self.mainConfig[self.SORTER_CONFIG][self.SAVE_INI]
        if res:
            self.saveINI = res

    def init_rules(self):
        self.rulesList = []
        for element in self.mainConfig[self.RULES]:
            try:
                enumBookAttr = ba.__getitem__(element)
                order = self.mainConfig[self.RULES][element]
                enemSortOrder = sord.__getitem__(order)
                sr = SortRule(enumBookAttr, enemSortOrder)
                self.rulesList.append(sr)
            except Exception as e:
                raise InvalidConfigAttr(element)

    def init_attributes(self):
        self.init_INIs()
        self.init_rules()

    def check_config_file(self):
        if self.is_valid_config():
            self.init_attributes()
        else:
            raise InvalidConfigFile(self.config_file)

    def configure(self):
        if self.mainConfig.read(self.config_file):
            self.check_config_file()
        else:
            raise FileNotFoundError(self.config_file)
