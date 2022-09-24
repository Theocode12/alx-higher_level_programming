#!/usr/bin/python3
"""
A Python script that takes in a URL and an email
sends a POST request to the passed URL with the
email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

from urllib import request
from urllib import parse
from sys import argv


def main():
    """main function"""

    data = {'email': argv[2]}
    data = parse.urlencode(data).encode()
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
        print(content)


if __name__ == '__main__':
    main()
