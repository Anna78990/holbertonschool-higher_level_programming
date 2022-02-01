#!/usr/bin/python3
""" check if they are the same class"""


def is_same_class(obj, a_class):
    """
    check if they are the same class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
