#!/usr/bin/python3
"python script that fetches https://alx-intranet.hbtn.io/status"
import urllib.request
import urllib.error


req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
try:
    with urllib.request.urlopen(req) as response:
        utf8_content = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(response))
        print("\t- content:", response.read())
        print("\t- utf8 content:", utf8_content)
except urllib.error.URLError as e:
    print(e.reason)
