#!/usr/bin/python3
"""A module that implements the getting the attributes
of a circular object"""
import math


class MagicClass:
    """A class that find the area and circumference of an
    object"""

    def __init__(self, radius=0):
        """Intializes the radius of object"""

        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Returns the area of the circle"""

        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""

        return ((2 * math.pi) * self._MagicClass__radius)
