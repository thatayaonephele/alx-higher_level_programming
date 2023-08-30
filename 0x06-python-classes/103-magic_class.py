#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode provided."""

from math import pi as p


class MagicClass:
    """This represents a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

          Args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) != float and type(radius) != int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Defined with the docstring"""
        return (self.__radius ** 2 * p)

    def circumference(self):
        """The docstring"""
        return (2 * p * self.__radius)
