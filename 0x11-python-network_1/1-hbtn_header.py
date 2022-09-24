#!/usr/bin/python3
"""
 Displays the value of the X-Request-Id variable
 found in the header of the response
"""
if __name__ == '__main__':
    from sys import argv
    from urllib import request

    with request.urlopen(argv[1]) as resp:
        X_Request_Id = resp.getheader('X-Request-Id')
        print(X_Request_Id)
