#!/usr/bin/python3
"""This module contains a class representing a Square"""


class Square:

    """A class used to represent a Square with the attribute size

        Attributes:
            size (int):size of square
            position (tuple):tuple of position
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        if len(position) != 2 or type(position[0]) is not int or\
           type(position[1]) is not int or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__size * self.__size

    def my_print(self):
        if len(self.__position) != 2 or type(self.__position[0]) is not int or\
           type(self.__position[1]) is not int or self.__position[0] < 0 or\
           self.__position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
        else:
            if self.__size == 0:
                print("")
            else:
                if self.__position[1] > 0:
                    for u in range(0, self.__position[1]):
                        print("")
                for i in range(0, self.__size):
                    for e in range(0, self.__position[0]):
                        print(" ", end="")
                    for z in range(0, self.__size):
                        print("#", end="")
                    print("")
