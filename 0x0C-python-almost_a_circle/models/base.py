#!/usr/bin/python3
"""This module contains a class representing Base"""

import json
class Base:
    """A class used to represent a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls)
        my_obj = self.to_json_string(list_objs)
        with open(filename, 'w+') as f:
            json.dump(my_obj, f)
