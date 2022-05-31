#!/usr/bin/python3
for num in range(97, 123):
    if chr(num) == 'q' or chr(num) == 'e':
        continue
    print("{:c}".format(num), end="")
