#!/usr/bin/python3
"""A class that defines elements of a matrix"""


def matrix_divided(matrix, div):
    """division operation on all matrix elements
    Args:
        matrix: matrix to be divided.
        div: number float or integer used to divide.
    Exception Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        The divided elements inside of a matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(my_row, list) for my_row in matrix) or
            not all((isinstance(my_element, float) or
                    isinstance(my_element, int))
                    for my_element in
                    [n for my_row in matrix for n in my_row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(my_row) == len(matrix[0]) for my_row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    const_var = 0
    if div == const_var:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), my_row)) for
            my_row in matrix])
