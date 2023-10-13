#!/usr/bin/python3

"""
    This module supplies the pascal_triangle
    function.
"""


def pascal_triangle(n):
    """
        This function returns the pascal
        triangle values from 1 to n.
    """
    if not isinstance(n, int):
        return

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if triangle:
            last_row = triangle[-1]

            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle
