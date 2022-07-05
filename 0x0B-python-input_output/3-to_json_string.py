#!/usr/bin/python3
"""A module that returns Json objects"""

import json
"""Importing The json module"""


def to_json_string(my_obj):
    """Converts an object to a json string"""

    j_obj = json.dumps(my_obj)
    return j_obj
