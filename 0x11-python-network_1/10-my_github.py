#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == '__main__':
    # set username and password variables with arguments passed
    username = sys.argv[1]
    passwd = sys.argv[2]

    # GitHub API URL to fetch user details
    git_url = "https://api.github.com/user"

    # send a request using basic_auth
    r = requests.get(git_url, auth=HTTPBasicAuth(username, passwd))
    if r.ok:
        data = r.json()
        print(f'{data.get("id")}')
    else:
        print('None')
