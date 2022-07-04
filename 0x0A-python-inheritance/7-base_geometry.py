#!/usr/bin/python3
"""A module thas creates a class BaseGeometry"""


class BaseGeometry(object):
    """A class named BaseGeometry"""

    def area(self):
        """Area of Base"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
