#!/usr/bin/python3
"""
A module for the method to_json_to-string serialization
"""


from json import dumps as d


def to_json_string(my_obj):
    """
    A function that returns a string object represented in JSON format
    """
    return (d(my_obj))
