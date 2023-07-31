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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float.")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float.")

    return int(a) + int(b)
