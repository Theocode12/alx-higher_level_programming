#!/usr/bin/python3
"""A module for multiplication of matrices"""


def matrix_mul(m_a, m_b):
    """find the product of two matrices

    args:
        m_a: matrix A
        m_b: matrix B

    Returns:"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not len(m_a):
        raise ValueError("m_a can't be empty")
    if not len(m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
        if not len(row):
            raise ValueError("m_a can't be empty")
        for cols in row:
            if type(cols) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        cmp_row = len(m_a[0])
        if cmp_row != len(row):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
        if not len(row):
            raise ValueError("m_b can't be empty")
        for cols in row:
            if type(cols) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        cmp_row = len(m_b[0])
        if cmp_row != len(row):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    nw_row = []
    value = 0
    for i in range(len(m_a)):
        nw_row = []
        for j in range(len(m_b[0])):
            value = 0
            for k in range(len(m_b)):
                value += m_a[i][k] * m_b[k][j]
            nw_row.append(value)
        result.append(nw_row)

    return result


if __name__ == '__main__':
    print(matrix_mul([[1, 2], [3, 4]], [[1.5, 2.5, 3.5], [4.5, 6.5, 7.5]]))
