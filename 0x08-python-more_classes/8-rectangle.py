#!/usr/bin/python3
"""
 Defines a rectangle class
"""


class Rectangle():
    """
    class Rectangle in which width and height are
    defined as Private instance attributes.
    Args:
        width (int): Horizonta side of a triangle
        height(int): Vertical side of a rectangle
    functions:
        __init__(self, width=0, height=0)
        height(self)
        width(self)
        height(self, value)
        width(self, value)
        perimeter(self)
        area(self)
        __str__(self)
        __del__(self)
        __repr__(self)
        bigger_or_equal(rect_1, rect_2)

    Public class attribute:
        number_of_instances (int): number of instances created and not deleted
        print_symbol (any type): used to print string representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialization function.
        Attributes:
            width(int): horizontal side of a rectangle.
            height(int): vertical side of a rectangle.
        Public class attribute:
            number_of_instances: Incremented during each
            new instance instantiation.
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """
        The function for private attribute width to retrieve it
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The function for private attribute width to set it
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value >= 0) is False:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The function for private attribute height to retrieve it
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The function for private attribute height to set it        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value >= 0) is False:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        A public instance method returning the rectangle
        """
        return int(self.__height) * int(self.__width)

    def perimeter(self):
        """
        A public instance method returning the rectangle perimeter
        """
        perimeter = ((self.__width + self.__height) * 2)

        if self.__height == 0:
            return 0
        elif self.__width == 0:
            return 0
        else:
            return perimeter

    def __str__(self):
        """
        Rectangle representation using the character #.
        """
        a = range(self.__height)
        b = str(self.print_symbol)
        if self.__height == 0:
            return ""
        elif self.__width == 0:
            return ""
        sym = '\n'.join([b * self.__width
                        for r in a])
        return sym

    def __del__(self):
        """
        Print a msg when an instance of Rectangle is deleted
        """
        self.__class__.number_of_instances -= 1
        print('Bye rectangle...')

    def __repr__(self):
        """
        returns string representation of rectangle
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A function that compairing 2 sizes of rectangles.
        Returns:
            biggest rectangle based on the area. rect_1 if both have
            the same area value.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        else:
            pass

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
            pass
        else:
            pass
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
