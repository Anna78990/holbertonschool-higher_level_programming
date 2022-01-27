#!/usr/bin/python3
"""

This module prints square

"""


def print_square(size):
    """
    print square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        if size == 0:
            print("")
        for i in range(0, size):
            for z in range(0, size):
                print("#", end="")
            print("")
