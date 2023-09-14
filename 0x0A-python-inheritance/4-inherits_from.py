#!/usr/bin/python3

""" A module that defines instance of a class verification
"""


def inherits_from(obj, a_class):

    """Returns true if object is inherited from specified class"""
    if issubclass(obj.__class__, a_class) is True:
        if obj.__class__ is a_class:
            return False
        else:
            return True
