#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_sum = 0
    for x in set(my_list):
        my_sum = my_sum + x
    return (my_sum)
