#!/usr/bin/python3

def inherits_from(obj, a_class):
    ac = type(obj)
    if a_class in ac.mro():
        if ac != a_class:
            return True
        else:
            return False
    else:
        return False
