#!/usr/bin/python3
def magic_calculation(a, b):

    """yteCode -> Python #3"""
    i = 4
    j = 6
    from magic_calculation_102 import sub, add
    if a > b:
        return (sub(a, b))
    else:
        ret_val = add(a, b)
        for x in range(i, j):
            ret_val = add(ret_val, x)
        return (ret_val)
