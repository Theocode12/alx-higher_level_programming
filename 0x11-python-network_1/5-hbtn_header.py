#!/usr/bin/python3
"""
A Python script that takes in a URL
sends a request to the URL and displays
the value of the variable X-Request-Id
in the response header
"""

from sys import argv
import requests


def main():
    """Main function"""

    resp = requests.head(argv[1])
    print(resp.headers.get('X-Request-Id'))


if __name__ == "__main__":
    main()
