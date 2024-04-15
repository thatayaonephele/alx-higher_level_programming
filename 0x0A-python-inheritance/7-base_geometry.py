#!/usr/bin/python3
"""
Defines a class module
"""


class BaseGeometry:
    """A Geometry of type class"""

    def integer_validator(self, name, value):
        """Verify value type"""
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))

    def area(self):
        """If area is not implemented,raise exception"""
        raise Exception('area() is not implemented')
