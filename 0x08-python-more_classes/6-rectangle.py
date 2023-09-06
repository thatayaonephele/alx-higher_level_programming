#!/usr/bin/python3
"""
    A class that represents a rectangle.
"""


class Rectangle:
    """
        class Rectangle defines a rectangle
        Attributes:
            height (int): height of the rectangle
            width (int): width of the rectangle
            number_of_instances (int): number
            of rectangle instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            A new rectangle initilization
            Args:
                height (int): height of the rectangle
                width (int): width of the rectangle
        """
        if isinstance(width, int):
            if (width >= 0) is False:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if (height >= 0) is False:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """
            Set the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Private instance attribute to set it
            Args:
                value (int): The new width representing the value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value >= 0) is False:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Sets the Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Private instance attribute to set it
            Args:
                value (int): The new value representing height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value >= 0) is False:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            A public instance method returning the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            A public instance method returning the rectangle perimeter
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """
            Instance method returning informal printable representing instance
            Represents the rectangle with the # character.

        """
        rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle
        g = self.__height - 1
        for x in range(g):
            rectangle = rectangle + "#" * self.__width + "\n"
        rectangle = rectangle + "#" * self.__width

        return rectangle

    def __repr__(self):
        """
            returns string representation of rectangle
            representation able to be recreated into a new instance
            using eval
        """
        rectangle = ''
        if self.__height == 0 or self.__width == 0:
            return rectangle
        rectangle = 'Rectangle({}, {})'.format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        """
            Print a msg when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print('Bye rectangle...')
