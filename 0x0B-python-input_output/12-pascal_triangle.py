#!/usr/bin/python3
"""
A module that returns the pascals triangle
"""


def pascal_triangle(n):
    """
    return the pascals triangle
    """

    p_tri = []
    if n <= 0:
        return p_tri
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                cols = p_tri[i - 1][j - 1] + p_tri[i - 1][j]
                row.append(cols)
        p_tri.append(row)
    return p_tri
