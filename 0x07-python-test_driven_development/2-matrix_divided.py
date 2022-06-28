#!/usr/bin/python3
"""A simple module that divides element of a matrix by
a divisor"""


def matrix_divided(matrix, div):
    """Divides elements of matrix by a divisor

    Args:
        matrix (list): A list of lists of integers

        div (int or float): The divisor of the elements

        Returns: a list of lists of integers or floats
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(matrix) is not list or type(matrix[0]) is not list:
        err = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(err)
    if not div:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row_size = len(matrix[0])
    for row in matrix:
        new_row = []
        if type(row) is not list:
            err = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(err)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            err = "matrix must be a matrix (list of lists) of integers/floats"
            if type(i) not in [int, float]:
                raise TypeError(err)
            new_row.append(round((i / div), 2))
        new_matrix.append(new_row)
    return new_matrix
