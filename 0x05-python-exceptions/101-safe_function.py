#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr as s
    try:
        x = fct(*args)
        return (x)
    except Exception:
        print("Exception: {}".format(Exception), file=s)
        return (None)
