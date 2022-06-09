#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [x ** 2 for x in row], matrix))
