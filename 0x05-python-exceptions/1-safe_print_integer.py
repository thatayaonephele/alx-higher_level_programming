#!/usr/bin/python3
def safe_print_integer(value):
    
    try:
        x = value
        print("{:d}".format(x))
        return (True)
    except ValueError:
        return (False)
