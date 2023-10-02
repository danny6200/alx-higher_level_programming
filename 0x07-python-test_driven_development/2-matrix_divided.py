#!/usr/bin/python3
"""
    This module supplies the matrix_divided function.

    Usage:
    ------
        >>> matrix_divided = __import__("2-matrix_divided").matrix_divided
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> print(matrix_divided(matrix, 2))
"""


def matrix_divided(matrix, div):
    """
        This function divides a 'matrix' by a number 'div'.

        Arguments:
        ----------
            matrix (a list of list of integers/floats): first argument
            div (an integer or float): second argument

        Return Value:
        -------------
            It returns a new matrix with each element divided
            and formatted to 2 decimal places
    """
    m = "matrix must be a matrix (list of lists) of integers/floats"
    # Check if matrix is NOT a list of lists of integers/floats
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix) and
            all(isinstance(i, (int, float)) for row in matrix for i in row)):
        raise TypeError(m)
    # Check if matrix rows have equal sizes
    elif not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check if div is non-numeric
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is 0
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(i / div, 2) for i in row] for row in matrix]
