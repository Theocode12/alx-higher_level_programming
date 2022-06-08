#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        sqr_mat = []
        for row in matrix:
            cln = []
            for i in row:
                cln.append(i ** 2)
            sqr_mat.append(cln)
        return sqr_mat
