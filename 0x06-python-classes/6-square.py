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

        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter for position of square"""

        return self._position

    @position.setter
    def position(self, value):
        """Setter for position of square"""
        print("position: {}".format(value))
        if not(len(value) == 2
            and type(value) is tuple
            and type(value[0]) is int
            and type(value[1]) is int
                and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self._position = value

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

    def my_print(self):
        """Prints a square"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" "*self.position[0], end="")
            print('#'*self.size)
