#!/usr/bin/python3
"""  script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from urllib import error, request
import sys


if __name__ == '__main__':
    # store url argumen passed in url varible
    url = sys.argv[1]
    # try and send a request and catch errors if any
    try:
        with request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    # catch and print error code
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
    except error.URLError:
        print('Index')
