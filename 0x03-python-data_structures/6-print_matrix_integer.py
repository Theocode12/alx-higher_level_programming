#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for element in mat:
            print("{:d}".format(element), end=' ')
        print()
