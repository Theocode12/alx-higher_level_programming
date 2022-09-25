#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

from sys import argv
import requests


def main():
    """Main function"""

    usr_name = argv[1]
    repo_name = argv[2]
    url = f"https://api.github.com/repos/{usr_name}/{repo_name}/commits"
    commits = requests.get(url).json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))


if __name__ == "__main__":
    main()
