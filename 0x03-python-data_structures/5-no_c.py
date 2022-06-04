#!/usr/bin/python3
def no_c(my_string):
    nw_str = ''
    for str in my_string:
        if str != 'c' and str != 'C':
            nw_str += str
    return nw_str
