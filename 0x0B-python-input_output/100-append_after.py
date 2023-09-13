#!/usr/bin/python3
"""A module that defines an insertion method"""


def append_after(filename="", search_string="", new_string=""):
    """ A function that appends text into a file
    """
    u = ""
    with open(filename) as f:
        for y in f:
            u = u + y
            if search_string in y:
                u = u + new_string
    with open(filename, "w") as w:
        w.write(u)
