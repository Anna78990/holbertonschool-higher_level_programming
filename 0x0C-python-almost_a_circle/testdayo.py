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
Square.save_to_file([Square(1)])
with open("Square.json", "r") as file:
    f = file.read()
print(f)
