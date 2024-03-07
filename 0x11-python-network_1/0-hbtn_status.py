#!/usr/bin/python3
"python script that fetches https://alx-intranet.hbtn.io/status"
import urllib.request
import urllib.error


if __name__ == '__main__':
    url_web = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url_web) as response:
            content = response.read()
            utf8_content = content.decode('utf-8')
            print("Body response:")
            print("\t- type:", type(content))
            print("\t- content:", content)
            print("\t- utf8 content:", utf8_content)
    except urllib.error.URLError as e:
        print(e.reason)
