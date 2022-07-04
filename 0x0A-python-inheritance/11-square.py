#!/usr/bin/python3
"""A module for square object"""

Rectangle = __import__('9-rectangle').Rectangle
"""Importing Rectangle class"""


class Square(Rectangle):
    """A square object"""

    def __init__(self, size):
        """Constructor for square object"""

        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Area of square object"""

        return self.__size ** 2

    def __str__(self):
        """Returns a user friendly string representation of the Square"""

        return "[Square] {}/{}".format(self.__size, self.__size)
