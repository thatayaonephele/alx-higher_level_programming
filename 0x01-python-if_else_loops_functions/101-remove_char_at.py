#!/usr/bin/python3
"""Remove at position"""


def remove_char_at(str, n):
    """create a copy of the string, remove char at the position n"""

    a = str[:n]
    b = str[n + 1:]
    if (n >= 0) is True:
        return (str)
    x = a + b
    return (x)
