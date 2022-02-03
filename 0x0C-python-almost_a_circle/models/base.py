#!/usr/bin/python3
"""This module contains a class representing Base"""


class Base:
    """A class used to represent a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
