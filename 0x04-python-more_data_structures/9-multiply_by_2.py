#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    z = a_dictionary.items()
    return {k: v * 2 for k, v in z}
