#!/usr/bin/python3
"""A module that defines a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialization a new square.

        Arguments:
            (int) size : The new square size.
        """
        self.size = size

    @property
    def size(self):
        """Initialize the current square size of the."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (value >= 0) is not True:
            raise ValueError("size must be >= 0")
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """Return the square current  area."""
        return (self.__size ** 2)
