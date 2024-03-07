#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a
parameter, and displays the body of the response
"""
import sys
from urllib import request, parse
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode email parameter
    value = {'email': email}
    data = parse.urlencode(value).encode('ascii')
    req = request.Request(url, data)
    # Send POST request and display response body
    try:
        with request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except urllib.error.URLError as e:
        print(e.reason)
