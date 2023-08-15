#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = (len(my_list))
    if x == 0:
        print ("{:d}".format(my_list))
    while x > 0:
        print("{:d}".format(my_list[x - 1]))
        x = x - 1
