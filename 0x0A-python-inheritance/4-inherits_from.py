#!/usr/bin/python3
"""A module that checks if an obj is a subclass of
a class"""


def inherits_from(obj, a_class):
    """check if obj is a subclass of a_class"""

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
