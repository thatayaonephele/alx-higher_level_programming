#!/usr/bin/python3
def safe_print_integer(value):

    x = value
    try:
        print("{:d}".format(x))
        return (True)
    except ValueError:
        return (False)
