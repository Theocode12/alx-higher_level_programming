#!/usr/bin/python3
"""
A Python script that takes in a URL
sends a request to the URL and
displays the body of the response
"""

from sys import argv
import requests


def main():
    """main function"""
    try:
        resp = requests.get(argv[1])
        resp.raise_for_status()
        print(resp.text)
    except Exception:
        print("Error code: {}".format(resp.status_code))


if __name__ == "__main__":
    main()
