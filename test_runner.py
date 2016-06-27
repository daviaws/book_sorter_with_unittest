import unittest

from tests.mainconfig_test import MainConfigTest
from tests.booksconfig_test import BooksConfigTest
from tests.sorter_test import SorterTest

def prepare_tests():
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(MainConfigTest))
    suite.addTests(loader.loadTestsFromTestCase(BooksConfigTest))
    suite.addTests(loader.loadTestsFromTestCase(SorterTest))

if __name__ == "__main__":
	prepare_tests()
	unittest.main()