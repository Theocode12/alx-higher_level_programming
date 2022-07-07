#!/usr/bin/python3
"""
A module that searchs and updates a text
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append after function to search
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i+1, new_string)

    with open(filename, mode="w", encoding="utf-8") as file:
        text = "".join(lines)
        file.write(text)
