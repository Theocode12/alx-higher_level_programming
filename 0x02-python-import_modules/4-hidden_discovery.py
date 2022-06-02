#!/usr/bin/python3
import hidden_4 as hd
if __name__ == '__main__':
    variables = dir(hd)
    for var in variables:
        if var[0] != "_":
            print(var)
