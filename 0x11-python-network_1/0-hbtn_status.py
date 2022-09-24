#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as resp:
    content = resp.read()
    obj_content = type(content)
    s_content = content.decode('utf-8')
    p_str = """Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"""
    print(p_str.format(obj_content, content, s_content))
