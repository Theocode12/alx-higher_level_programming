#!/usr/bin/python3
"""A module that write to a file"""


def write_file(filename="", text=""):
    """Write to a file"""

    with open(filename, mode="w", encoding="utf-8") as f_name:
        size = f_name.write(text)
    return size
