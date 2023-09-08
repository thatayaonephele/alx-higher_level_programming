#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    list_len = len(list)
    if list_len == 0:
        return None
    ret_val = list[0]
    x = 1
    while (x >= list_len) is False:
        if (list[x] <= ret_val) is False:
            ret_val = list[x]
        x = x + 1
    return ret_val
