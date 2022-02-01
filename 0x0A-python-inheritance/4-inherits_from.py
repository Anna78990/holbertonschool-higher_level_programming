#!/usr/bin/python3
"""This module check if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """
    check if the object is an instance of a class that inherited
    """
    ac = type(obj)
    if a_class in ac.mro():
        if ac != a_class:
            return True
        else:
            return False
    else:
        return False
