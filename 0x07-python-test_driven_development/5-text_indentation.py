#!/usr/bin/python3
"""A module which print a text with 2 new lines after characters:
., ?, :"""


def text_indentation(text):
    """Prints text according to specificaation

    Args:
        text: a string

        Returns:
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    e_text = []
    e_str = ""
    for char in text:
        e_str += char
        if char in ['.', '?', ':']:
            e_text.append(e_str.strip(' '))
            e_str = ""
    e_text.append(e_str.strip(' '))
    for i, line in enumerate(e_text):
        if i < (len(e_text) - 1):
            print(line)
            print()
        else:
            print(line, end="")
