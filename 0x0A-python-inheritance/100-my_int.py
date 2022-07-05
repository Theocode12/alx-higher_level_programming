#!/usr/bin/python3
"""The rebel class MyInt"""


class MyInt(int):
    """A class which inherits from the class int"""

    def __eq__(self, other):
        """compare MyInt object when == is used"""

        int.__eq__(self, other)
        if int(self) is other:
            return False
        return True

    def __ne__(self, other):
        """Is called when the != is used"""

        int.__ne__(self, other)
        if int(self) is other:
            return True
        return False
