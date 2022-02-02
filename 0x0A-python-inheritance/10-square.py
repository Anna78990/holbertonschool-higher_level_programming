#!/usr/bin/python3
"""this module contains class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """
    class Sqaure
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super(Square, self).__init__(size, size)
