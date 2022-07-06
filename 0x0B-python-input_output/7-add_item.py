#!/usr/bin/python3
"""A script that adds all arguements in to a python list."""

from sys import argv
"""Importing the sys and os module"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
"""Importing the save_to_json module"""

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""Importing the load_from_json module"""

filename = "add_item.json"
args = argv
if len(args) > 1:
    args = args[1:]
else:
    args = []
try:
    text = load_from_json_file(filename)

except Exception:
    text = []


for arg in args:
    text.append(arg)
save_to_json_file(text, filename)
