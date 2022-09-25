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
    url = "https://api.github.com/repos/" \
          + usr_name + '/' + repo_name + '/commits'
    commits = requests.get(url).json()[:10]
    for commit in commits:
        if type(commit) is dict:
            sha = commit.get('sha')
            name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))


if __name__ == "__main__":
    main()
