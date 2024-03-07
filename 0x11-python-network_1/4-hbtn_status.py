#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    # fetch url using get request
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\ttype: {type(r)}')
    print(f'\tcontent: {r.content}')
