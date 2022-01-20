#!/usr/bin/python3
"""This module contains a class representing a Square"""


class Square:

    """A class used to represent a Square with the attribute size

        Attributes:
            size (int):size of square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        ss = self.__size
        if type(self.__size) is not int and ss.isdigit is False:
            raise TypeError('size must be an integer')
        elif int(self.__size) < 0:
            raise ValueError('size must be >= 0')
        else:
            return int(self.__size) * int(self.__size)
