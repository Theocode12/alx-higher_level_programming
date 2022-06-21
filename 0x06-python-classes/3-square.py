#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module demonstrates the use of classes by
creating a square class
"""


class Square(object):
    """A class use to represent a square Object"""

    def __init__(self, size=0):
        """Initialize a square object"""

        if (isinstance(size, int)) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """Return the area of this square"""

        return self._Square__size ** 2
