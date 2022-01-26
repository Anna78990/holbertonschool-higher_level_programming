#!/usr/bin/python3
"""

This module contains the function which can devide elements

"""


def say_my_name(first_name, last_name=""):
    """
    say your name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
