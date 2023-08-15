#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    x = len(my_list)
    max_val = my_list[x - 1]
    if (x == 0):
        return (None)
    if ((x) == 1):
        max_val = my_list[0]
    return (max_val)
