#!/usr/bin/python3
"""
A Python script that takes in a URL
sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib import error
from sys import argv


def main():
    """Main function"""
    try:
        with request.urlopen(argv[1]) as resp:
            content = resp.read().decode('utf-8')
            print(content)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main()
