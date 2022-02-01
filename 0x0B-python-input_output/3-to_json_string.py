#!/usr/bin/python3
"""
this module returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    this module returns the JSON representation of an object (string)
    my_obj(dict): object to convert
    Return: JSON representation
    """
    return json.dumps(my_obj)
