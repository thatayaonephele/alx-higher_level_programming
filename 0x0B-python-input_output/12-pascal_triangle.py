#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """A function that defines Pascal's triangle of size n"""
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    tri = [[1]]

    # Build the triangle row by row
    while len(tri) < n:
        prev_row = tri[-1]  # Get the last row
        temp = [1]  # Start each row with a 1
        for x in range(len(prev_row) - 1):
            temp.append(prev_row[x] + prev_row[x + 1])  # Calculate the new value
        temp.append(1)  # End each row with a 1
        tri.append(temp)  # Append the new row to the triangle

    return tri
