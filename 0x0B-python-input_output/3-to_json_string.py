#!/usr/bin/python3
import json
"""
this module returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    this module returns the JSON representation of an object (string)
    my_obj(dict): object to convert
    Return: JSON representation
    """
    return json.dumps(my_obj)
