#!/usr/bin/python3

def uppercase(str):
    a = 97
    b = 122
    c = 32
    for x in str:
        if ord(x) <= b and ord(x) >= a:
            x = chr(ord(x) - c)
        print("{:s}".format(x), end='')
    print('\n', end="")
