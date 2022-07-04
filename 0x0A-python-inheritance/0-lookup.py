#!/usr/bin/python3
"""A module to check for available attributes and methods"""


def lookup(obj):
    """A function that returns a list of availble attributes and methods
    of an object"""

    return list(dir(obj))
