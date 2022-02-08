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
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string representation of square """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter of size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter of size"""
        self.width = value
        self.height = value

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
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
            return
        else:
            if len(kk) > 0:
                for k, v in kwargs.items():
                    if k == "id":
                        self.id = v
                    if k == "size":
                        self.width = v
                        self.height = v
                    if k == "x":
                        self.x = v
                    if k == "y":
                        self.y = v

    def to_dictionary(self):
        """ convert to dict """
        return dict(id=self.id, x=self.x, size=self.width, y=self.y)
