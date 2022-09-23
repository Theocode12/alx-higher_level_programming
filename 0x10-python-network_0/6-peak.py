#!/usr/bin/python3
"""A module that calculates a peak in a list of unsorted integers"""


def find_peak(list_int):
    """
    A function that finds a peak in a list of unsorted integers
    """

    for i in range(len(list_int)):
        if i > 0 and list_int[i] < list_int[i - 1]:
            return list_int[i - 1]
    if list_int:
        return list_int[0]
