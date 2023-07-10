#!/usr/bin/python3
"""
Contains the MyList class
"""


class MyList(list):
    """A subclass of list that has a print_sorted method"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
