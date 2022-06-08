#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary)
    for key in dict:
        print("{}: {}".format(key, a_dictionary.get(key)))
