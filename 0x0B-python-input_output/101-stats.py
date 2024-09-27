#!/usr/bin/python3
"""
A module that logs the parsing of scripts.
"""

import sys


def check_match(line, script_size, status_codes):
    """
    A function that parses a line of log input and updates the metrics.

    Args:
        line (str): The log line.
        script_size (list): A list containing the total size of files.
        status_codes (dict): A dictionary with status codes as keys.
    """
    try:
        line = line.strip()  # Remove newline and other trailing characters
        parts = line.split(" ")
        # Update the total script size
        script_size[0] += int(parts[-1])
        # Get the status code and update its count if valid
        status_code = int(parts[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    except (ValueError, IndexError):
        pass


def print_stats(script_size, status_codes):
    """
    Prints the accumulated statistics.

    Args:
        script_size (list): A list containing the total size of files.
        status_codes (dict): A dictionary with status codes as keys.
    """
    print("File size: {}".format(script_size[0]))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    script_size = [0]  # Using a list to maintain a mutable total size
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    line_count = 0  # To count the number of lines processed

    try:
        for line in sys.stdin:
            check_match(line, script_size, status_codes)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(script_size, status_codes)
    except KeyboardInterrupt:
        print_stats(script_size, status_codes)
        raise
    print_stats(script_size, status_codes)
