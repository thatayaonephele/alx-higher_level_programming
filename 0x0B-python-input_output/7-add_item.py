#!/usr/bin/python3
# 9-add_item.py
"""A function that adds argument into alist and is saved in a python file
from sys import argv as av
"""

if __name__ == "__main__":
    save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
        y = 1
    items.extend(av[y:])
    save_to_json_file(items, "add_item.json")
