#!/usr/bin/python3
"""This module contains a class representing a Square"""


class Rectangle:

    """A class used to represent a Square with the attribute size
        Attributes:
            size (int):size of square
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        if type(self.__width) is not int or type(self.__height) is not int:
            raise TypeError('size must be an integer')
        elif self.__width < 0 or self.__height < 0:
            raise ValueError('size must be >= 0')
        else:
            return self.__width * self.__height

    def perimeter(self):
        if type(self.__width) is not int or type(self.__height) is not int:
            raise TypeError('size must be an integer')
        elif self.__width < 0 or self.__height < 0:
            raise ValueError('size must be >= 0')
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if type(self.__width) is not int or type(self.__height) is not int:
            raise TypeError('size must be an integer')
        elif self.__width < 0 or self.__height < 0:
            raise ValueError('size must be >= 0')
        else:
            rec = []
            if self.__width == 0 or self.__height == 0:
                return ""
            for i in range(0, self.__height):
                for z in range(0, self.__width):
                    rec.append(str(self.print_symbol))
                if i != (self.__height - 1):
                    rec.append("\n")
            return ''.join(rec)

    def __repr__(self):
        rect = 'Rectangle(' + str(self.__width) + ',' + str(self.__height)\
            + ')'
        return rect

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        x = rect_1.height * rect_1.width
        y = rect_2.height * rect_2.width
        if y < x:
            return rect_1
        elif y == x:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
