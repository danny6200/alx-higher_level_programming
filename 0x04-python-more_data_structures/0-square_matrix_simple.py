#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return matrix
    new_matrix = []
    for row in matrix:
        squared = map(lambda x: x**2, row)
        new_matrix.append(list(squared))
    return new_matrix
