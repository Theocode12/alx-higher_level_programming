#!/usr/bin/python3
"""A module that reads a file and prints it"""


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as f_name:
        print(f_name.read())