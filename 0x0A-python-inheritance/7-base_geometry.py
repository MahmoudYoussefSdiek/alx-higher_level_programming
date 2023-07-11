#!/usr/bin/python3
"""
Contains the BaseGeometry class
"""


class BaseGeometry:
    """
    A class with an unimplemented area method and an integer validator method
    """

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name: a string
            value: an integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
