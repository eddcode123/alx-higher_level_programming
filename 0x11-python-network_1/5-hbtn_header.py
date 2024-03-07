#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys

if __name__ == '__main__':
    # save url passed as argument in url varibale
    url = sys.argv[1]
    # send request to url
    req = requests.get(url)
    if 'X-Request-Id' in req.headers:
        print(req.headers['X-Request-Id'])
