#!/usr/bin/python3
"""
Contains the MyInt class
"""


class MyInt(int):
    """A subclass of int that has == and != operators inverted"""

    def __eq__(self, other):
        """Returns True if self and other are not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns True if self and other are equal"""
        return super().__eq__(other)
