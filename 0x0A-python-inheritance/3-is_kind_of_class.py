#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines an inherited class checking function & a class
"""


def is_kind_of_class(obj, a_class):
    """Verify if obj is an inherited instance of a class or instance
    """
    if not isinstance(obj, a_class):
        return False
    return True
