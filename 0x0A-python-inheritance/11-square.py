#!/usr/bin/python3
"""Module that defines a Square class, derived from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that models a square shape."""

    def __init__(self, size):
        """Constructor to create a new square instance.

        Args:
            size (int): The length of one side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
