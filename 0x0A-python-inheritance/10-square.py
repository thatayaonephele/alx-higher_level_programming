#!/usr/bin/python3
"""Square class that is a subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class to model a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Create a square with a specified size.

        Args:
            size (int): The dimension of the square (its side length).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
