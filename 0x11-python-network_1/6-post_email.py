#!/usr/bin/python3
"""  script that takes in a URL and an email address,
sends a POST requestto the passed URL with the email
as a parameter, and finally displays the body of the response.
"""
import requests
import sys


if __name__ == '__main__':
    # store email and url in respective variables
    url = sys.argv[1]
    email = sys.argv[2]

    # send a post request to url
    values = {'email': email}
    req = requests.post(url, data=values)
    print(req)
