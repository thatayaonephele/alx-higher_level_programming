#!/usr/bin/python3
"""This is a module that defines a funciton of  file-writing type"""


def write_file(filename="", text=""):
    """A function that writes a string to a utf-8 textfile
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
