#!/usr/bin/python3

class BaseGeometry():

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
                raise TypeError("{} must be an integer".format(name))
        if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
        return "[Rectangle] {} / {}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height

class Square (Rectangle):
    def __init__(self, size):
        super(Square, self).__init__(size, size)
