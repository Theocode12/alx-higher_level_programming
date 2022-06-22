#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module demonstrates the use of classes by
creating a square class
"""


class Square(object):
    """A class use to represent a square Object"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object"""

        self._Square__size = size
        self._Square__position = position

    @property
    def position(self):
        """Getter for position of square"""

        return self._Square__position

    @position.setter
    def position(self, value):
        """Setter for position of square"""

        if not(len(value) == 2 and value[0] >= 0 and value[1] >= 0
            and isinstance(value, tuple)
            and isinstance(value[1], int)
                and isinstance(value[2], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

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
            return
        for i in range(self._Square__position[1]):
            print()
        for i in range(self._Square__size):
            print(" "*self._Square__position[0], end="")
            print('#'*self._Square__size)
