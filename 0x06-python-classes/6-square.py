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

        self._Square__position = position
        self._Square__size = size

    @property
    def _Square__position(self):
        """Getter for position of square"""

        return self.__Square__position

    @_Square__position.setter
    def _Square__position(self, value):
        """Setter for position of square"""

        if (len(value) == 2 and value[0] >= 0 and value[1] >= 0
            and isinstance(value, tuple)
            and isinstance(value[0], int)
                and isinstance(value[1], int)):
            self.__Square__position = value
            return
        raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def _Square__size(self):
        """A getter function that retrieves a private variable"""

        return self.__Square__size

    @_Square__size.setter
    def _Square__size(self, value):
        """A setter variable used to set a private variable"""

        if (isinstance(value, int)) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__Square__size = value

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
