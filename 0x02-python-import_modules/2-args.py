#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    if len(argv) - 1 == 1:
        print("{} argument:".format(len(argv) - 1))
    elif len(argv) - 1 > 0:
        print("{} arguments:".format(len(argv) - 1))
    else:
        print("0 arguments.")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
