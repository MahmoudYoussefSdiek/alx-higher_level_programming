#!/usr/bin/python3
"""This module defines the Base class"""


class Base:
    """
    Base class for managing the id attribute in future classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the
        number of objects created.
                            It is initialized to 0.

    Methods:
        __init__(self, id=None): Class constructor method.
                                 If id is provided, assigns it to the
                                 public instance attribute 'id'.
                                 If id is not provided, increments
                                 __nb_objects and assigns the new
                                 value to 'id'.
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
