#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
            return
        for i, n in enumerate(row):
            print("{:d}".format(n), end=" " if i < len(row) - 1 else "\n")
        print()
