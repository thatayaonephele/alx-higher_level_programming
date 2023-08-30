#!/usr/bin/python3
"""
This module defines a class square with public
attribute area and private instance attribute size
"""


class Square:
    """
    class Square in which size is defined as
    Private instance attribute.

    Argumentss:
        (int) size : The inner square size

    Methods:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """
        Function that initializates a new square

        Attr:
            (int)__size: the square size of a side.

        If size is less than 0, raise a ValueError exception
        with the message "size must be >= 0."

        Size must be an integer, else raise a TypeError
        exception with the message "size must be an integer."

        """
        if (size >= 0) is not True:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size

    def area(self):
        """
        Method Function that determines the square current area.

        Returns:
            The current area of the square
        """
        return int(self.__size)**2
