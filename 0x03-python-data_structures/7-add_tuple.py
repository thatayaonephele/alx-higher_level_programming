#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()): 
    my_tup = ()
    x = tuple_a + (0, 0)
    y = tuple_b + (0, 0)
    my_tup = x[0] + y[0], x[1] + y[1]
    return my_tup
