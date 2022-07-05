#!/usr/bin/python3
"""This module inherits the list object and uses it
to sort list items"""


class MyList(list):
    """This class add more functionality to the list object"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
