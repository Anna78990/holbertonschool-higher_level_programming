#!/usr/bin/python3
"""
this module returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    this returns the dictionary description with simple data structure
    obj(class): class to read
    return: dictionary description
    """
    return obj.__dict__
