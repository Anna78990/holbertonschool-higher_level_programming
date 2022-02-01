#!/usr/bin/python3
""" 
this module returns an object represented by JSON
"""


import json
def from_json_string(my_str):
    """
    this module returns an object represented by JSON
    my_obj(dict): JSON represantation to convert
    Return: object represented by JSON
    """
    return json.loads(my_str)
