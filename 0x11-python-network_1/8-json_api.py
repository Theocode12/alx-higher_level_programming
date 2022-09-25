#!/usr/bin/python3
"""
A Python script that takes in a letter
and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

from sys import argv
import requests


def main():
    """Main function"""

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}
    r = requests.post(url, data)
    try:
        py_obj = r.json()
        if not py_obj:
            print("No result")
            return
        print("[{}] {}".format(py_obj.get('id'), py_obj.get('name')))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
