#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle using BaseGeometry('7-base_geometry')."""

    def __init__(self, width, height):
        """Instantiate a new Rectangle.
        Args:
            width (int): New Rectangle width.
            height (int): New Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """Return informal print() and str() representation of Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string = string + str(self.__width) + "/" + str(self.__height)
        return string
