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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        le = len(list_objs)
        my_obj = []
        for i in range(0, le):
            my_obj.append(list_objs[i].to_dictionary())
        with open(filename, 'w+') as f:
            f.write(cls.to_json_string(my_obj))

    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        return dummy.update(dictionary)
