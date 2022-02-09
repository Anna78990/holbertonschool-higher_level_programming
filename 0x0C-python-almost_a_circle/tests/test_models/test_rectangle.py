#!/usr/bin/python3
""" Unittest of Rectangle class"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """ Test of class Rectangle """

    def test_init_rectangle(self):
        """test method for initialisation of rectangle
        """
        r = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 0, 0, 1)


if __name__ == "__main__":
    unittest.main()
