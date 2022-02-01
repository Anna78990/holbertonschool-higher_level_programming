#!/usr/bin/python3
"""
this module returns the dictionary description with simple data structure
"""


import json


def class_to_json(obj):
    """
    this returns the dictionary description with simple data structure
    obj(class): class to read
    return: dictionary description
    """
    return json.dumps(obj.__dict__)
