import sys

from src.mainconfig import MainConfig
from src.sorter import ListSorter
from src.book import Book

def main(config_file):
    mC = MainConfig(config_file)
    list_sorter = ListSorter()
    books = mC.get_books()
    rules = mC.get_rules()
    sorted_books = list_sorter.sort(books, rules)
    print('In:  {}'.format(books))
    print('Out: {}'.format(sorted_books))
    mC.save_books(sorted_books)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = 'config.ini'
    main(config_file)
