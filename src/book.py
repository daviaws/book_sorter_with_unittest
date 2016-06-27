from enum import Enum

class BookAttributes(Enum):
    
    code = 'code'
    title = 'title'
    author = 'author'
    edition_year = 'edition_year'

class Book():

    def __init__(self, title, author, edition_year, code):
        '''
        A book encapsulation
        Parameters:
        Strings:
            title
            author
            edition_year
        Integer:
            code
        '''
        self.title = title
        self.author = author
        self.edition_year = edition_year
        self.code = code

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and \
                    self.author == other.author and \
                    self.edition_year == other.edition_year and \
                    self.code == other.code
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return str(self.code)
