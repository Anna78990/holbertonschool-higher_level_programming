#!/usr/bin/python3
""" Unittest of Base class"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """ Test of class Base """

    def test_id(self):
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(3)
        self.assertEqual(b.id, 3)

    