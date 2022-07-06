#!/usr/bin/python3
"""A module that save to a json file."""

import json
"""Importing json module"""


def save_to_json_file(my_obj, filename):
    """Save to a json file."""

    with open(filename, 'w', encoding='utf-8') as j_file:
        json.dump(my_obj, j_file)
