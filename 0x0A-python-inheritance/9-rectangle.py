#!/usr/bin/python3
"""this module contains class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
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
