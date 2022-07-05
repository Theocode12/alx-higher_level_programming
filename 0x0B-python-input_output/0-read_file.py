#!/usr/bin/python3
"""A module that reads a file and prints it"""


def read_file(filename=""):
    """A function that reads a file and prints it"""

    if type(filename) is str:
        with open(filename, mode="r", encoding="utf-8") as f_name:
            print(f_name.read(), end="")
