#!/usr/bin/python3
"""A function that lists avail attr & methods of an object"""

def lookup(obj):


    """Return: A lookup function returning an object's list"""
    x = dir(obj)
    return (x)
