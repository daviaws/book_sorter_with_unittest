import unittest

from .reference_books_test import *

from src.book import BookAttributes as ba
from src.sorter import ListSorter, SortRule, SortingServiceException, SortOrder as sord

class SorterTest(unittest.TestCase):

    loaded_books = [b1,b2,b3,b4]
    list_sorter = ListSorter()

    def test_author_ascending_title_descendig_sort(self):
        print()
        print('### Sorter Test ###')
        print('Test author ascending title descending sort')
        r1 = SortRule(ba.author, sord.ascending)
        r2 = SortRule(ba.title, sord.descending)
        rules = [r1,r2]
        expected_books = [b1,b4,b3,b2]
        result = self.list_sorter.sort(self.loaded_books, rules)
        self.assertEqual(expected_books, result)

    def test_edition_descending_author_descending_title_ascendig_sort(self):
        print()
        print('Test edition descending author descending title ascending sort')
        r1 = SortRule(ba.edition_year, sord.descending)
        r2 = SortRule(ba.author, sord.descending)
        r3 = SortRule(ba.title, sord.ascending)
        rules = [r1,r2,r3]
        expected_books = [b4,b1,b3,b2]
        result = self.list_sorter.sort(self.loaded_books, rules)
        self.assertEqual(expected_books, result)

    def test_empty_rules_sort(self):
        print()
        print('Test empty rules sort')
        rules = []
        expected_books = []
        result = self.list_sorter.sort(self.loaded_books, rules)
        self.assertEqual(expected_books, result)

    def test_none_rules_sort(self):
        print()
        print('Test none rules sort')
        rules = None
        try:
            result = self.list_sorter.sort(self.loaded_books, rules)
        except Exception as e:
            self.assertEqual(SortingServiceException, type(e))

    def test_title_ascendig_sort(self):
        print()
        print('Test title ascending sort')
        r1 = SortRule(ba.title, sord.ascending)
        rules = [r1]
        expected_books = [b3,b4,b1,b2]
        result = self.list_sorter.sort(self.loaded_books, rules)
        self.assertEqual(expected_books, result)
