#!/usr/bin/python3
"""Module that defines the MyInt class, a subclass of int."""


class MyInt(int):
    """Class that inverts the behavior of the == and != operators."""

    def __eq__(self, value):
        """Override the == operator to behave like !=."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator to behave like ==."""
        return self.real == value
