#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    c = a_dictionary.get(key)
    if c is not None:
        del a_dictionary[key]
    return (a_dictionary)
