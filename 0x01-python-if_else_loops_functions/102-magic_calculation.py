#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return a
    if c > b:
        return a + b
    return a * b - c
