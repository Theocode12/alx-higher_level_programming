#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    max_val = my_list[0]
    for max in my_list:
        if max >= max_val:
            max_val = max
    return max_val
