#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """Representation of a rectangle.

    Attributes:
        number_of_instances (int): Count of current Rectangle instances.
        print_symbol (any): Symbol used to represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter/setter for the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter/setter for the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determine which rectangle has the larger area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.
        Raises:
            TypeError: If either argument is not an instance of Rectangle.
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new square-shaped rectangle.

        Args:
            size (int): Dimensions of the square.
        """
        return cls(size, size)

    def __str__(self):
        """String representation of the rectangle using print_symbol."""
        if not self.__width or not self.__height:
            return ""

        rect = []
        for i in range(self.__height):
            rect.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """String representation for development/debugging purposes."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Handle actions when an instance is deleted."""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

