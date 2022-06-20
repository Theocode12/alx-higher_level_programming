#!/usr/bin/python3
from asyncio import exceptions


def safe_print_division(a, b):
    flag = 1
    try:
        result = a / b
    except ZeroDivisionError:
        flag -= 1
    finally:
        if flag:
            print("Inside result: {:.1f}".format(result))
            return result
        print("Inside result: None")
