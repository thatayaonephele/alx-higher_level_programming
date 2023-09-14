#!/usr/bin/python3
"""
A module that defines the is_same_class method
"""


def is_same_class(obj, a_class):
    """
    return True if object is a exact instance of the specified class else False
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
