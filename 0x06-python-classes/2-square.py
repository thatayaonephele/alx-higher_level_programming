#!/usr/bin/python3
""" This module defines a class Square """


class Square:
    """
        A class Square that represents a square by: (based on 1-square.py)
        Attr:
            size (no type or value identification): The square size
        Method Type:
            __init__: init of size attribute for each instance
    """
    def __init__(self, size=0):
        """ Instantiation with optional size
            Arguments:
                (int) size : The square size
        """
        if (isinstance(size, int)):
            self.__size = size
            if (size >= 0) is not True:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
