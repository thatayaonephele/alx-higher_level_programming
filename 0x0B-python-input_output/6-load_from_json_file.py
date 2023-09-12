#!/usr/bin/python3
"""A module that defines a json file"""
from json import load as ld


def load_from_json_file(filename):
    """An object method that defines a JSON file"""
    with open(filename) as f:
        return ld(f)
