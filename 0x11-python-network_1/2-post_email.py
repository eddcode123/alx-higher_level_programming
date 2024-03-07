#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a
parameter, and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    # Check if URL and email arguments are provided
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Encode email parameter
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    # Send POST request and display response body
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            print("Your email is:", content)
    except urllib.error.URLError as e:
        print(e.reason)
