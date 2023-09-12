#!/usr/bin/python3
"""
A module for a method called save_to_json_file
"""


from json import dump as dp


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file, using a JSON rep
    """
    with open(filename, "w",) as json_file:
        dp(my_obj, json_file)
