#!/usr/bin/python3
"""A module that load a json file"""

import json
"""Importing the json module"""


def load_from_json_file(filename):
    """loads py object from json file"""

    with open(filename, 'r', encoding='utf-8') as j_obj:
        py_obj = json.load(j_obj)
    return py_obj
