#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda row: [x * x for x in row], matrix))
