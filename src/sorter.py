from enum import Enum

class SortOrder(Enum):
   
    ascending = 'ascending'
    descending = 'descending'

class SortRule():
   
    def __init__(self, enumAttr, enumOrder):
        '''
        A rule to sort
        Parameters:
        enumAttr = an enum attribute name of an object to sort
        enumOrder = an enum from SortOrder
        '''
        self.attribute = enumAttr.value
        self.order = enumOrder

class SortingServiceException(Exception):
    pass

class ListSorter():
    '''
    Sort service to the technical assessment from stormtech
    '''

    def sort(self, aList, rules):
        '''
        Sort a list of objects based in a list of rules.
        Parameters:
        aList = list of objects to be sorted
        rules = list of SortRule in order of priority
        Returns:
        If receives the list of rules:
            The list ordered
        If the rules are an empty list:
            An empty list
        '''
        if rules == None:
            raise SortingServiceException

        aList = list(aList)
        if rules:
            rules.reverse() #Minor priority are done first
            for rule in rules:
                aList.sort(key = lambda obj: obj.__getattribute__(rule.attribute))
                if SortOrder.descending == rule.order:
                    aList.reverse()
        else:
            aList = []
        return aList
