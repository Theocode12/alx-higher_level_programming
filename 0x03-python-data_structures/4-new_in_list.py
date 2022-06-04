#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    nw_cp = my_list.copy()
    nw_cp[idx] = element
    return nw_cp
