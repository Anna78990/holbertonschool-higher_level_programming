#!/usr/bin/python3
"""This module contains a class representing Base"""


class Base:
    """A class used to represent a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

class Rectangle(Base):

    @staticmethod
    def int_valid(**kwargs):
        for k, v in kwargs.items():
            if k == "width" or k == "height":
                if type(v) != int:
                    raise TypeError("{} must be an integer".format(k))
                if v <= 0:
                    raise ValueError("{} must be > 0".format(k))
            else:
                if type(v) != int:
                    raise TypeError("{} must be an integer".format(k))
                if v < 0:
                    raise ValueError("{} must be >= 0".format(k))


    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.int_valid(width=width, height=height, x=x, y=y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.int_valid(width=value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.int_valid(height=value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.int_valid(x=value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.int_valid(y=value)
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        if self.__width == 0 or self.__height == 0:
            print("")
        if self.__y > 0:
            for u in range(0, self.__y):
                print("")
        for i in range(0, self.__height):
            for e in range(0, self.x):
                print(" ", end="")
            for z in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
    .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        le = len(args)
        if le == 0:
            return
        for i in range(0, le):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.__width = args[1]
            if i == 2:
                self.__height = args[2]
            if i == 3:
                self.__x = args[3]
            if i == 4:
                self.__y = args[4]

    def to_dictionary(self):
        return dict(x = self.__x, y = self.__y, id = self.id, height = self.__height, width = self.__width)
