#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    req = requests.get(url)
    req = req.json()

    for x in req[:10]:
        print(x.get('sha'), end=': ')
        print(x.get('commit').get('author').get('name'))
