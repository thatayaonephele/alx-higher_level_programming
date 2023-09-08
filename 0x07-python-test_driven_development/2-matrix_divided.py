#!/usr/bin/python3
""" A class that defines elements of a matrix """


def matrix_divided(matrix, div):
    """
        division operation on all matrix elements
        Args:
            div: number used to divide
            matrix: matrix to be divided
        Return:
            The divided elements inside of a matrix
    """
    if (type(matrix) != list):
        raise TypeError(
            'matrix must be a matrix (list of lists)of integers/floats'
             )
    """ test for uniform list length """
    it = iter(matrix)
    length = len(next(it))
    if not all(len(length) == length for length in it):
        raise TypeError('Each row of the matrix must have the same size')
    """ A function that does 'list values' checks """
    for y in matrix:
        for x in y:
            if not isinstance(x, int) or isinstance(x, float) or x is None:
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats'
                     )
    """ A function that checks for division """
    if not isinstance(div, int) or isinstance(div, float) or div is None:
        raise TypeError('div must be a number')
    if (div != 0) is False:
        raise ZeroDivisionError('division by zero')
    """otherwise : divide the matrix by 2 to 2 dp"""
    return([list(map(lambda i: round(i / div, 2), x))for x in matrix])
