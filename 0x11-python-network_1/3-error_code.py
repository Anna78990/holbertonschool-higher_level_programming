#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""
from urllib.request
from urllib.error
import sys

if __name__ == "__main__":
    req = urllib.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode("utf8"))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
    except urllib.error.URLError as e:
        print('Error code: ', e.code)
