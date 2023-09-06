#!/usr/bin/python3
"""Defines a class of Rectangle type"""


class Rectangle:
    """A class that represents a rectangle."""

    def __init__(self, width=0, height=0):
        """A new rectangle initilization

        Args:
            height (int): The height of the new rectangle.
            width (int): The width of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Sets the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value >= 0) is False:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Sets the Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value >= 0) is False:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public instance method returning the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """A public instance method returning the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Instance method returning informal printable representing instance

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        my_rect = []
        for z in range(self.__height):
            [my_rect.append('#') for a in range(self.__width)]
            if z != self.__height + (-1):
                my_rect.append("\n")
        return ("".join(my_rect))

    def __repr__(self):
        """Returns the string representation of the Rectangle."""

        my_rect = "Rectangle(" + str(self.__width)
        my_rect = my_rect + ", " + str(self.__height) + ")"
        return (my_rect)

    def __del__(self):
        """Print a msg when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
