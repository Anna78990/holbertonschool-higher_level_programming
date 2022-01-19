#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    boo = key in a_dictionary
    if boo is True:
        a_dictionary.pop(key)
    return a_dictionary
