#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    z = sorted(a_dictionary.items())
    for x, y in z:
        print('{}: {}'.format(x, y))
