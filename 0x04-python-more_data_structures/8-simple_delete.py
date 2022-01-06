#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        removed_value = a_dictionary.pop(key)
        return removed_value
    else:
        return a_dictionary
