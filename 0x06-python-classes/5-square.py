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

        self._Square__size = size

    @property
    def size(self):
        """A getter function that retrieves a private variable"""

        return self._Square__size

    @size.setter
    def size(self, value):
        """A setter variable used to set a private variable"""

        if (isinstance(value, int)) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """Return the area of this square"""

        return self._Square__size ** 2

    def my_print(self):
        """Prints a square"""
        if self._Square__size == 0:
            print()
        for i in range(self._Square__size):
            print('#'*self._Square__size)
