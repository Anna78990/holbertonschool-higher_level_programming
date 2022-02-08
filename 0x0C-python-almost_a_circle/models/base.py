#!/usr/bin/python3
"""This module contains a class representing Base"""

import json
import os


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
        if list_dictionaries is not None and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        my_obj = []
        if list_objs is not None:
            le = len(list_objs)
            for i in range(0, le):
                my_obj.append(list_objs[i].to_dictionary())
        with open(filename, 'w+') as f:
            f.write(cls.to_json_string(my_obj))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        is_file = os.path.isfile(filename)
        if is_file is True:
            with open(filename, 'r') as f:
                json_s = f.read()
            json_list = cls.from_json_string(json_s)
            list_insta = []
            for json_dic in json_list:
                list_insta.append(cls.create(**json_dic))
            return list_insta
        else:
            return []
