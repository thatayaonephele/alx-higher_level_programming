#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """A new rectangle initilization
            Args:
                height (int): height of the rectangle
                width (int): width of the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __del__(self):
        """Print a msg when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Used to retrieve the private instnce attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Used to set the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value >= 0) is False:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Used to retrieve the private instnce attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Used to set the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value >= 0) is False:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public instance method returning the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """A public instance method returning the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """Instance method returning informal pirintable reping of instance"""
        s = ""
        g = str(self.print_symbol)
        z = range(self.__height)
        if self.__height != 0 and self.__width != 0:
            s = s + "\n".join(g * self.__width for y in z)
        return s

    def __repr__(self):
        """returns string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
