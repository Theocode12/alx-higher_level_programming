#!/usr/bin/python3
"""A simple module which add two integers or floats"""


def add_integer(a: int, b: int = 98) -> int:
    """Find the sum of two integers.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns: sum of two integers"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
