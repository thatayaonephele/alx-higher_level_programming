#!/usr/bin/python3
'''Defines a square
'''


def add_integer(a, b=98):
    '''Executes the sum of 2 integers.
    Args:
        b (int, optional): The second number.
        a (int): The first number.
    Return:
        The sum of the two integers.
    '''
    if type(a) != int or float:
        raise TypeError('a must be an integer')
    elif type(b) != int or float:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
