#!/usr/bin/python3
"""
A Python script that fetches
https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """Main Function"""

    resp = requests.get("https://alx-intranet.hbtn.io/status")
    p_str = "Body response:\n\t- type: {}\n\t- content: {}"
    print(p_str.format(type(resp.text), resp.text))


if __name__ == "__main__":
    main()
