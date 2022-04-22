#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=value)
    print(response.text)
