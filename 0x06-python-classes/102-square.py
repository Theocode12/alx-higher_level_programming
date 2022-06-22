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

        self.size = size

    @property
    def size(self):
        """A getter function that retrieves a private variable"""

        return self._size

    @size.setter
    def size(self, value):
        """A setter variable used to set a private variable"""

        if (isinstance(value, int)) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return the area of this square"""

        return self.size ** 2

    def __eq__(self, others):
        """Check if the area of two square objects are same"""

        if isinstance(others, Square):
            return True if self.size == others.size else False
        else:
            return False

    def __ne__(self, others):
        """Check if the area of two square objects are  not same"""

        if isinstance(others, Square):
            return True if self.size != others.size else False
        else:
            return False

    def __lt__(self, others):
        """Check if the area of a square object is less than the other"""

        if isinstance(others, Square):
            return True if self.size < others.size else False
        else:
            return False

    def __gt__(self, others):
        """Check if the area of a square object is greater than the other"""

        if isinstance(others, Square):
            return True if self.size > others.size else False
        else:
            return False

    def __le__(self, others):
        """Check if the area of a square object is less
        than or equal to the other"""

        if isinstance(others, Square):
            return True if self.size <= others.size else False
        else:
            return False

    def __ge__(self, others):
        """Check if the area of a square object is greater
        than or equal the other"""

        if isinstance(others, Square):
            return True if self.size >= others.size else False
        else:
            return False
