#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    # store url passed as argument
    my_url = sys.argv[1]
    # send a request to the url
    try:
        with urllib.request.urlopen(my_url) as response:
            if 'X-Request-Id' in response.headers:
                print(response.headers['X-Request-Id'])
    except urllib.error.URLError as e:
        print(e.reason)
