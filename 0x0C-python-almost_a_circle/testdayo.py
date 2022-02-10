#!/usr/bin/python3
""" Unittest of Rectangle class"""
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

capturedOutput = io.StringIO()
sys.stdout = capturedOutput
r1 = Rectangle(2, 3, 2, 2)
r1.display()
sys.stdout = sys.__stdout__
a = capturedOutput.getvalue()
print(a)
