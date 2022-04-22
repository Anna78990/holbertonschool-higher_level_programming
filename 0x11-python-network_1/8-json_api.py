#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        value = {'q': ''}
    else:
        value = {'q': sys.argv[1]}

    response = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        j = response.json()
        if j == {}:
            print("No result")
        else:
            print("[{}] {}".format(j.get("id"), j.get("name")))
    except ValueError:
        print("Not a valid JSON")
