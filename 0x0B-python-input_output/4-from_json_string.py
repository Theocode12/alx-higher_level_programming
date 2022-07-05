#!/usr/bin/python3
"""A module that converts from Json string to Python object."""

import json
"""Importing the json module"""


def from_json_string(my_str):
    p_obj = json.loads(my_str)
    return p_obj
