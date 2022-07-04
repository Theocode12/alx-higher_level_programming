#!/usr/bin/python3
"""A module that checks if an object is an instance of a class
that inherited from another class"""


def is_kind_of_class(obj, a_class):
    """Checks if an obj is a kind of class"""

    return isinstance(obj, a_class)
