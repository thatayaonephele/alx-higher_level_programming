#!/usr/bin/python3
# 9-add_item.py

"""
This script adds all command-line arguments to a Python list
and saves the updated list to a JSON file named add_item.json.
If the file does not exist, it will be created.
"""

import sys

if __name__ == "__main__":
    # Import functions for saving and loading JSON data
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Attempt to load existing items from add_item.json, create an empty list if it fails
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add new command-line arguments to the list (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to add_item.json
    save_to_json_file(items, "add_item.json")
