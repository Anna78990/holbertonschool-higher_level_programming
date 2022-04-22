#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('ascii'))
