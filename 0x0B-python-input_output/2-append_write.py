#!/usr/bin/python3
"""A module that append a text to a file"""


def append_write(filename="", text=""):
    """Append a text to a file"""

    with open(filename, mode="a", encoding="utf-8") as f_name:
        size = f_name.write(text)
    return size
