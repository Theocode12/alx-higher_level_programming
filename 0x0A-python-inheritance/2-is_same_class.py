#!/usr/bin/python3
"""A module that returns a boolean value indicating
if an object is of a particular class"""


def is_same_class(obj, a_class):
    """checks if an object is of the class a_class"""

    if type(obj) is a_class:
        return True
    return False
