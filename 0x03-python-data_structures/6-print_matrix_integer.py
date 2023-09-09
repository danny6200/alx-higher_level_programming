#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, n in enumerate(row):
            print("{}".format(n), end=" " if i < len(row) else "\n")
        print()
