#!/usr/bin/python3
"""
A module that return a dictionary of a class
"""


def class_to_json(obj):
    my_dict = obj.__dict__
    for key in my_dict:
        if key[-2:] == "__":
            del my_dict[key]
    return my_dict
