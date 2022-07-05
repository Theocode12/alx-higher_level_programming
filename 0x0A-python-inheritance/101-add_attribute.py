#!/usr/bin/python3
"""set atrribute module"""


def add_attribute(self, name, value):
    """add attribute function"""

    if hasattr(self, '__dict__'):
        setattr(self, name, value)
    else:
        raise TypeError("can't add new attribute")
