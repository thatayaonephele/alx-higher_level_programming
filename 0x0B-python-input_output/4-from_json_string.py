#!/usr/bin/python3
"""
A module that defines a method from_json_string type
"""


from json import loads as lo


def from_json_string(my_str):
    """
    Returns: A module that represents a json string
    """
    return (lo(my_str))
