#!/usr/bin/python3
def islower(c):
    x = 97
    y = 122
    z = ord(c)
    if z <= y and z >= x:
        return True
    else:
        return False
