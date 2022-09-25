#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials
(username and password) and uses the GitHub API
to display your id
"""

from sys import argv
import requests


def main():
    """main function"""
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(argv[1], argv[2]))
    print(resp.json().get('id'))


if __name__ == "__main__":
    main()
