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
        """test method for id of base
        """
        b = Base()
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()
