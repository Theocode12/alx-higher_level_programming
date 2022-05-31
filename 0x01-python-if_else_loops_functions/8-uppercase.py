#!/usr/bin/python3
def uppercase(str):
    """Convert a string to uppercase."""
    for char in str:
        char = ord(char)
        if char > 96 and char <= 122:
            char = char - 32
        print("{:c}".format(char), end="")
    print()
