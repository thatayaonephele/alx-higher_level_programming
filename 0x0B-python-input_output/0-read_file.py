#!/usr/bin/python3

"""A function that reads a file
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
