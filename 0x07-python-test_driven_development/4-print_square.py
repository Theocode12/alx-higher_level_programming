#!/usr/bin/python3
"""A module that prints a square with a #"""


def print_square(size):
    """Prints the size of square if its possible

    Args:
        size: size of square

        Returns:
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
