#!/usr/bin/python3
"""A script that adds all arguements in to a python list."""

import sys
"""Importing the sys and os module"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""Importing the save_to_json module"""

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""Importing the load_from_json module"""


args = sys.argv
if len(args) > 1:
    args = args[1:]
else:
    args = []
try:
    text = load_from_json_file("add_item.json")
    if len(text) == 0:
        text = []

except:
    save_to_json_file(args, "add_item.json")

else:
    for arg in args:
        text.append(arg)
    save_to_json_file(text, "add_item.json")
