#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode("utf8"))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
