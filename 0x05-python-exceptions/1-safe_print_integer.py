#!/usr/bin/python3
def safe_print_integer(value):
    
    try:
        print("{:d}".forma(t(value)))
        return (True)
    except ValueError:
        return (False)
