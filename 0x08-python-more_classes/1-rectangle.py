#!/usr/bin/python3
"""Module that defines the Rectangle class."""


class Rectangle:
    """Class to represent a rectangle shape."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width 

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not (type(value) is int):
            raise TypeError("width must be an integer")
        if value > 0 is False:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not (type(value) is int):
            raise TypeError("height must be an integer")
        if value > 0 is False:
            raise ValueError("height must be >= 0")
        self.__height = value
