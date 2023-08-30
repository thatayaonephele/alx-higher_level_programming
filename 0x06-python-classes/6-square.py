#!/usr/bin/python3
"""A module that defines a class Square."""


class Square:
    """A square representation."""

    def __init__(self, size=0, position=(0, 0)):
        """The new square initialization.

        Arguments:
        (int) size : The new square size.
        position (int, int): The new square position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Define the square's current size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (value >= 0) is True:
            raise ValueError("size must be >= 0")
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        self.__size = value

    @property
    def position(self):
        """Define the square's current position."""
        return (self.__position)

    @position.setter
    def position(self, value):
        len_val = len(value)
        if (not isinstance(value, tuple) or
                len_val != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        result = self.__size * self.__size
        return (result)

    def my_print(self):
        """Print the square using # characters."""
        if (self.__size == 0):
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")
