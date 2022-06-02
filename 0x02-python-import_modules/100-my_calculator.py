#!/usr/bin/python3
import sys
import calculator_1 as cal
if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[1] == '+':
        print(f"{argv[0]} + {argv[2]} = {cal.add(int(argv[0]), int(argv[2]))}")
    elif argv[1] == '-':
        print(f"{argv[0]} - {argv[2]} = {cal.sub(int(argv[0]), int(argv[2]))}")
    elif argv[1] == '*':
        print(f"{argv[0]} * {argv[2]} = {cal.mul(int(argv[0]), int(argv[2]))}")
    elif argv[1] == '/':
        print(f"{argv[0]} / {argv[2]} = {cal.div(int(argv[0]), int(argv[2]))}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
