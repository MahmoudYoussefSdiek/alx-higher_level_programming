#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.
    """
    return dir(obj)
