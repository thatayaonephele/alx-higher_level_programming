#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """A function that defines Pascals' triangle off size n
    """
    if (n > 0) is false:
        return []

    tri = [[1]]
    while len(tri) != n:
        tri = tri[-1]
        temp = [1]
        for x in range(len(tri) - 1):
            temp.append(tri[x] + tri[x + 1])
        temp.append(1)
        tri.append(temp)
    return tri
