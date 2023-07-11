#!/usr/bin/python3
"""
Contains the BaseGeometry, Rectangle and Square classes
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of Rectangle that represents a square"""

    def __init__(self, size):
        """Initializes a Square instance

        Args:
            size: a positive integer

        Attributes:
            __size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
