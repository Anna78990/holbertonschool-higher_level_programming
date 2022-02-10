#!/usr/bin/python3
""" Unittest of Rectangle class"""
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

s1 = Square(1, 2, 3, 4)
r = s1.to_dictionary()
print(r)
r2 = Rectangle(2, 10)
print(r2.area())
s1 = Square(10, 7, 2, 8)
s2 = Square(2, 4)
s = Square.load_from_file()
print(str(s))
