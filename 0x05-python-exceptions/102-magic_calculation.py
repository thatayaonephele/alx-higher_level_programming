#!/usr/bin/python3
def magic_calculation(a, b):
    ret_val = 0
    for x in range(1, 3):
        try:
            if (x < a) is False:
                raise Exception('Too far')
            ret_val = ret_val + a ** b / x
        except Exception:
            ret_val = b + a
            break
    return (ret_val)
