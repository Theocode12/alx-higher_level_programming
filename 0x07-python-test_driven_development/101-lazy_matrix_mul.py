#!/usr/bin/python3
"""A module for multiplication of matrices using numpy"""

import numpy as np
"""Importing the numpy module"""


def lazy_matrix_mul(m_a, m_b):
    """find the product of two matrices

    args:
        m_a: matrix A
        m_b: matrix B

    Returns:"""

    return np.matmul(m_a, m_b)
