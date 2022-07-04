#!/usr/bin/python3
"""A module Rectangle for BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Importing BaseGeometry class"""


class Rectangle(BaseGeometry):
    """A rectangle class"""

    def __init__(self, width, height):
        """Initialize a variables for rectangle class"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """Returns a user friendly string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
