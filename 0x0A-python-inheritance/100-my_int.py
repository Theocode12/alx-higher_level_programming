#!/usr/bin/python3
"""The rebel class MyInt"""


class MyInt(int):
    """A class which inherits from the class int"""

    def __eq__(self, other):
        """compare MyInt object when == is used"""

        return int.__ne__(self, other)

    def __ne__(self, other):
        """Is called when the != is used"""

        return int.__eq__(self, other)
