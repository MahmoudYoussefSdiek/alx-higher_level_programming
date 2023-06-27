#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0):
        """Initializes the Square instance with a size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
