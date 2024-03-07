""" script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == '__main__':
    # store url argument to url varibale
    url = sys.argv[1]
    # send get resuest to url
    req = requests.get(url)
    if int(req.status_code) >= 400:
        print(f'Error code: {req.status_code}')
    else:
        print(req.text)
