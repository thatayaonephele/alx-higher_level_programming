#!/usr/bin/python3
def simple_delete(my_dict, x=""):
    if x in my_dict:
        del my_dict[x]
    return (my_dict)
