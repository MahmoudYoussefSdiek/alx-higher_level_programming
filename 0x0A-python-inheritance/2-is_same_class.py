#!/usr/bin/python3
"""
Contains the is_same_class function
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class

    Args:
        obj: any object
        a_class: any class
    """
    return type(obj) is a_class
