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
        text = []
        for line in lines:
            text.append(line)
            if search_string in line:
                text.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as file:
        text = "".join(text)
        file.write(text)
