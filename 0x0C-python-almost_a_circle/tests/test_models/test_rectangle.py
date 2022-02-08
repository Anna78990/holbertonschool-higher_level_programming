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
        self.assertEqual(r, r2)
        r = Rectangle(1, 2, 3)
        r2 = Rectangle(1, 2, 3, 0, 1)
        self.assertEqual(r, r2)
        r = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4, 1)
        self.assertEqual(r, r2)
        r = Rectangle(1, 2, 3, 4, 5)
        r2.update(**{ 'id': 5 })
        self.assertEqual(r, r2)

    def test_init_rectangle_type_error(self):
        """test method for check type error case of rectangle
        """
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_init_rectangle_value_error(self):
        """test method for check value error case of rectangle
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def area(self):
        """test method for the calculation of area
        """
        r2 = Rectangle(2, 10)
        self.assertEqual(r2, 20)
  
    def test_update_by_args(self):
        """test method update the instance by args
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        r2 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1, r2)
        r1.update(89, 1)
        r2 = Rectangle(1, 10, 10, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(89, 1, 2)
        r2 = Rectangle(1, 2, 10, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(89, 1, 2, 3)
        r2 = Rectangle(1, 2, 3, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(89, 1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(r1, r2)

    def test_update_by_kwargs(self):
        """test method update the instance by **kwargs
       	"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{ 'id': 89 })
        r2 = Rectangle(10, 10, 10, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(**{ 'id': 89, 'width': 1 })
        r2 = Rectangle(1, 10, 10, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        r2 = Rectangle(1, 2, 10, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        r2 = Rectangle(1, 2, 3, 10, 89)
        self.assertEqual(r1, r2)
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        r2 = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(r1, r2)


if __name__ == "__main__":
    unittest.main()
