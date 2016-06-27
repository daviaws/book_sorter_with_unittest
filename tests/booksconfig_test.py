import unittest

from .reference_books_test import *

from src.mainconfig import InvalidConfigAttr, InvalidConfigFile
from src.booksconfig import BooksConfig

CONFIG_PATH = 'books.ini'

class BooksConfigTest(unittest.TestCase):
    
    def test_booksINI_valid(self):
        print()
        print('### Books Configuration tests ###')
        print('Testing if booksINI is valid')
        try:
            bC = BooksConfig(CONFIG_PATH)
        except Exception as e:
            if InvalidConfigFile == type(e):
                print(e)
                raise
            if InvalidConfigAttr == type(e):
                print(e)
                raise

    def test_loading_books(self):
        print()
        print('Testing loading the books')
        expected_list = [b1,b2,b3,b4]
        try:
            bC = BooksConfig(CONFIG_PATH)
        except:
            pass
        else:
            self.assertEqual(expected_list, bC.bookList)
