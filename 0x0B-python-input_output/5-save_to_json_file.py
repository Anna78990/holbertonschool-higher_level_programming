#!/usr/bin/python3
"""
this module writes an Object to a text file, using a JSON representation:

"""


import json


def save_to_json_file(my_obj, filename):
    """
    this module returns the JSON representation of an object (string)
    my_obj(dict): object to convert
    """
    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
