#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class

    Args:
        obj: any object
        a_class: any class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
