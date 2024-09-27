#!/usr/bin/python3
"""Module to convert class instances to JSON serializable dictionaries.
"""

def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object's attributes.
    """
    return obj.__dict__
