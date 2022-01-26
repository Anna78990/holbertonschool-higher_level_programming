#!/usr/bin/python3
"""

This module contains the function which can add the numbers

"""


def add_integer(a, b=98):
    """
    addition
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
