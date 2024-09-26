#!/usr/bin/python3
"""Module that defines a function to add attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if allowed.

    Args:
        obj (any): The target object to which the attribute will be added.
        att (str): The name of the attribute to be added.
        value (any): The value to assign to the attribute.
    
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
