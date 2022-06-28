#!/usr/bin/python3
"""A module that prints your full name in a neatly
formatted way"""


def say_my_name(first_name: str, last_name: str = "") -> str:
    """Prints full name neatly formatted

    Args:
        first_name: Firstname

        last_name: Lastname

        Returns: formatted full name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
