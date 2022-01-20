#!/usr/bin/python3
"""This module contains a class representing a Square"""


class Square:

    """A class used to represent a Square with the attribute size"""

    _size = 0
    def __init__(self, size):

        """
        initialize square attributes

        Attributes:
            size(int):size of square

        """

        self.__size = size
