#!/usr/bin/python3
def islower(c):
    """Check if c is lowercase"""
    if ord(c) > 96 and ord(c) <= 122:
        return True
    else:
        return False
