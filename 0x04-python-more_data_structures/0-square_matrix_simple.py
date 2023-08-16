#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    y = len(matrix)
    if y == 0:
        return (matrix)
    return ([[n * n for n in m] for m in matrix])
