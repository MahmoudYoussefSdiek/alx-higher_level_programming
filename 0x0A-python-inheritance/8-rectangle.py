#!/usr/bin/python3
"""
Contains the BaseGeometry and Rectangle classes
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of BaseGeometry that represents a rectangle"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance

        Args:
            width: a positive integer
            height: a positive integer

        Attributes:
            __width: the width of the rectangle
            __height: the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
