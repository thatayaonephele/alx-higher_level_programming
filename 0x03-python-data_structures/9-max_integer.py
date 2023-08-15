#!/usr/bin/python3
def max_integer(my_list=[]):
    str_len = len(my_lst)
    if (str_len) == 0:
        return (None)
    x = my_list[0]
    for y in my_list:
        if x < y:
            x = y
    return (x)
