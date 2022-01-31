#!/usr/bin/python3
"""This module contains a class representing a Square"""


class MyList(list):

    """A class used to represent a Square with the attribute size
        Attributes:
            size (int):size of square
    """

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
