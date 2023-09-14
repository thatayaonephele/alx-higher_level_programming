#!/usr/bin/python3
"""A module that defines a  Geometry class"""


class BaseGeometry:
    """A function that returns an integer validator """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (value > 0) is False:
            raise ValueError("{} must be greater than 0".format(name))
