#!/usr/bin/python3
"""A function that defines addition of integers."""


def add_integer(a, b=98):
    """Execute the addition of b and a in integer format.
    Typecast all arguments of float type to integer prior to adding them together.
    Raises:
        TypeError: If b or a is a non-float and non-integer type.
    """
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    return (int(b) + int(a))
