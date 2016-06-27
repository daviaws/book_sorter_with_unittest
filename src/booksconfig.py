from configparser import ConfigParser

from .mainconfig import InvalidConfigAttr, InvalidConfigFile
from .book import Book, BookAttributes as ba

class BooksConfig():

    AUTHOR = ba.author.value
    EDITION_YEAR = ba.edition_year.value
    MANDATORY_CONFIGS = [AUTHOR, EDITION_YEAR]

    def __init__(self, booksINI):
        '''
        Read a INI with the books registereds
        '''
        self.booksINI = booksINI
        self.booksConfig = ConfigParser()
        self.bookList = None

        self.configure()

    def get_books(self):
        return list(self.bookList)

    def init_attributes(self):
        code = 1
        self.bookList = []
        for title in self.booksConfig.sections():
            author = self.booksConfig[title][self.AUTHOR]
            if not author:
                raise InvalidConfigAttr(author)
            edition_year = self.booksConfig[title][self.EDITION_YEAR]
            if not edition_year:
                raise InvalidConfigAttr(edition_year)
            book = Book(title, author, edition_year, code)
            self.bookList.append(book)
            code += 1

    def is_valid_config(self):
        for title in self.booksConfig.sections():
            for element in self.MANDATORY_CONFIGS:
                if not element in self.booksConfig[title]:
                    return False
            return True
        return False

    def check_config_file(self):
        if self.is_valid_config():
            self.init_attributes()
        else:
            raise InvalidConfigFile(self.booksINI)

    def configure(self):
        if self.booksConfig.read(self.booksINI):
            self.check_config_file()
        else:
            raise FileNotFoundError(config_file)
