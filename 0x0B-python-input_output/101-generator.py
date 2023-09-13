#!/usr/bin/python3
"""
A module that logs the parsing scripts
"""


from sys import stdin as st


if __name__ == "__main__":
    script_size = [0]
    c = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''A function that looks for a matching regular expression line'''
        try:
            line = line[:-1]
            tmp = line.split(" ")
            script_size[0] = script_size[0] + int(tmp[-1])
            result = int(tmp[-2])
            if result in c:
                c[result] = c + 1
        except ValueError:
            pass

    def print_stats():
        """Prints out the accumulated stats."""
        print("File size: {}".format(script_size[0]))
        for k in sorted(c.keys()):
            if c[k]:
                print("{}: {}".format(k, c[k]))
    x = 1
    b = 0
    a = 10
    try:
        for pos in st:
            check_match(pos)
            if x % a == b:
                print_stats()
            x = x + 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
