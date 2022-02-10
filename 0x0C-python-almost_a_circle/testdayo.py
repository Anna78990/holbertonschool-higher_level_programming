#!/usr/bin/python3
""" Unittest of Rectangle class"""
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

r1 = Rectangle.create(**{ 'id': 89 })
print(r1)
