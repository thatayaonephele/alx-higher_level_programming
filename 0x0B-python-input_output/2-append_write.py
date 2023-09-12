#!/usr/bin/python3
"""A module that defines a function of file-appending type"""


def append_write(filename="", text=""):
    """A function that appends a string to the end of an  encoded UTF8 file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
