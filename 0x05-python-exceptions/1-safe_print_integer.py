#!/usr/bin/python3
def safe_print_integer(value):

    x = isinstance(value, int)
    try:
        if x:
            print("{:d}".format(value))
            return (True)
    except ValueError:
        return (False)
