#!/usr/bin/python3

"""
A class MyList that inherits from list.
"""


class MyList(list):
    """
    Return: Displayed list, but sorted (ascending sort).
    """
    def print_sorted(self):
        """
        A function that prints list data sorted
        """
        x = sorted(self)
        print(x)
