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
s1 = Square(4, 6, 2, 1)
print(s1)
