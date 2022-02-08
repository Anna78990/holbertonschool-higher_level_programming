#!/usr/bin/python3
""" class Square """
from models.rectangle import Rectangle


class Square(Rectangle):

    """
    A class used to represent a Rectangle
    Attributes:
        size (int): size of rectangle
        x (int): x of rectangle
        y (int): y of rectangle
        id (int): id of the instance
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor of Square class """
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = id
        super(Square, self).__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.__x, self.__y, self.__size)

    @property
    def size(self):
        """ getter of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of size"""
        Rectangle.int_valid(width=value)
        self.__size = value

    def update(self, *args, **kwargs):
        """ update an instance """
        le = len(args)
        kk = kwargs.keys()
        if le == 0 and len(kk) == 0:
            return
        if le > 0:
            for i in range(0, le):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.__size = args[1]
                if i == 2:
                    self.__x = args[2]
                if i == 3:
                    self.__y = args[3]
            return
        else:
            if len(kk) > 0:
                for k, v in kwargs.items():
                    if k == "id":
                        self.id = v
                    if k == "size":
                        self.__size = v
                    if k == "x":
                        self.__x = v
                    if k == "y":
                        self.__y = v

    def to_dictionary(self):
        """ convert to dict """
        return dict(id=self.id, x=self.__x, size=self.__size, y=self.__y)
