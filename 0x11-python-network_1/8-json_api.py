#!/usr/bin/python3
"""  script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == '__main__':
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": q}
    url = 'http://0.0.0.0:5000/search_user'

    req = requests.post(url, data=payload)
    try:
        j_dict = req.json()
        if j_dict:
            print(f'[{j_dict['id']}] {j_dict['name']}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
