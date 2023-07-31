#!/usr/bin/python3
"""
This is the "0-add_integer" module.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First integer.
        b (int or float): Second integer (default is 98).
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
