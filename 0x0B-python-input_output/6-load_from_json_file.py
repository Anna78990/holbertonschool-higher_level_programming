#!/usr/bin/python3
"""
this module creates an Object from a “JSON file”

"""


import json


def load_from_json_file(filename):
    """
    this module creates an Object from a “JSON file”
    filename(str): file to read
    return: object from json
    """
    with open(filename, 'r') as f:
        return json.load(f)
