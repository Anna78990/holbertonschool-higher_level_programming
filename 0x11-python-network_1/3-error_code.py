#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Error code: ', e.code)
    else:
        with urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode("utf8"))
