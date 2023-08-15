#!/usr/bin/python3
def max_integer(my_list=[]):
    x = len(my_list)
    if (x == 0):
        return (None)
    if ((x) == 1):
        max_val = my_list[0]
    my_list.sort()
    max_val = my_list[x - 1]
    return (max_val)
