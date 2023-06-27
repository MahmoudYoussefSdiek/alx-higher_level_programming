#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square instance with a size and position."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or position[0] < 0 or \
                not isinstance(position[1], int) or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """Retrieves the size of the Square instance."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square instance."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the Square instance."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the Square instance."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or value[0] < 0 or \
                not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
