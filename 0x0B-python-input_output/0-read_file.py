#!/usr/bin/python3

"""A function that reads a file
"""


def read_file(filename=""):
    """
    A function that reads in data and prints to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
