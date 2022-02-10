#!/usr/bin/python3
""" Unittest of Rectangle class"""
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

r1 = Rectangle(1, 2, 3, 4, 5)
r = r1.to_dictionary()
print(r)
r2 = Rectangle(2, 10)
print(r2.area())
