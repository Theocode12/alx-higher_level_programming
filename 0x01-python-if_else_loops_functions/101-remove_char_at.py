#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) > n:
        cp_str = str[:n] + str[n + 1:]
        return cp_str
    return str
