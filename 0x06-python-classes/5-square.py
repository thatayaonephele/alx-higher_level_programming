#!/usr/bin/python3
"""This defines a class Square."""


class Square:
    """
    Square: defines a square.
    Attr:
    size (int): size of square.
    Method Function:
    __init__ : init of size attribute for each instance.
    """
    def __init__(self, size=0):
        """Initialize a new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter

    def size(self, value):
        """This gets or sets the current size of the square."""
        if (value < 0):
            raise ValueError('size must be >= 0')
        if (isinstance(value, int)) is not True:
            raise TypeError('size must be an integer')
        self.__size = value

    def area(self):
        """
        area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """This prints the square with the # character."""
        if (self.size <= 0) is not True:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
