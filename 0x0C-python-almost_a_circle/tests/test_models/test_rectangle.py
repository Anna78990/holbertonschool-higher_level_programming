#!/usr/bin/python3
""" Unittest of Rectangle class"""
import io
import sys
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
        self.assertEqual(r.height, r2.height)

    def test_init_rectangle2(self):
        """test method for initialisation of rectangle
        """
        r = Rectangle(1, 2, 3)
        r2 = Rectangle(1, 2, 3, 0)
        self.assertEqual(r.width, r2.width)

    def test_init_rectangle3(self):
        """test method for initialisation of rectangle
        """
        r = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, r2.x)

    def test_init_rectangle4(self):
        """test method for initialisation of rectangle
        """
        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, r2.id)
    
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

    def test_update(self):
        r1 = Rectangle(2, 3, 4, 5, 1)
        r1.update()
        r2 = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(r1.y, r2.y)

    def test_update_by_args(self):
        """test method update the instance by args
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        r2 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.width, r2.width)

    def test_update_by_args2(self):
        """test method update the instance by args
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1)
        r2 = Rectangle(1, 10, 10, 10, 89)
        self.assertEqual(r1.id, r2.id)

    def test_update_by_args3(self):
        """test method update the instance by args
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1, 2)
        r2 = Rectangle(1, 2, 10, 10, 89)
        self.assertEqual(r1.width, r2.width)

    def test_update_by_args4(self):
        """test method update the instance by args
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1, 2, 3)
        r2 = Rectangle(1, 2, 3, 10, 89)
        self.assertEqual(r1.height, r2.height)

    def test_update_by_args5(self):
        """test method update the instance by args
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(r1.x, r2.x)

    def test_update_by_kwargs(self):
        """test method update the instance by **kwargs
       	"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{ 'id': 89 })
        r2 = Rectangle(10, 10, 10, 10, 89)
        self.assertEqual(r1.id, r2.id)

    def test_update_by_kwargs2(self):
        """test method update the instance by **kwargs
       	"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{ 'id': 89, 'width': 1 })
        r2 = Rectangle(1, 10, 10, 10, 89)
        self.assertEqual(r1.width, r2.width)

    def test_update_by_kwargs3(self):
        """test method update the instance by **kwargs
       	"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        r2 = Rectangle(1, 2, 10, 10, 89)
        self.assertEqual(r1.height, r2.height)

    def test_update_by_kwargs4(self):
        """test method update the instance by **kwargs
       	"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        r2 = Rectangle(1, 2, 3, 10, 89)
        self.assertEqual(r1.x, r2.x)

    def test_update_by_kwargs5(self):
        """test method update the instance by **kwargs
       	"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        r2 = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(r1.y, r2.y)

    def test_string(self):
        """test method check __str()__
       	"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        strr = r1.__str__()
        strrr = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(strr, strrr)

    def test_display(self):
        """test method check output of display
       	"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        a = capturedOutput.getvalue()
        b = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(a,b)

    def test_display2(self):
        """test method check output of display
       	"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 3, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        a = capturedOutput.getvalue()
        b = "  ##\n  ##\n  ##\n"
        self.assertEqual(a,b)

    def test_display3(self):
        """test method check output of display
       	"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(2, 3)
        r1.display()
        sys.stdout = sys.__stdout__
        a = capturedOutput.getvalue()
        b = "##\n##\n##\n"
        self.assertEqual(a,b)

    def create_rectangle(self):
        """test method create new instance
        """
        r1 = Rectangle.create(**{ 'id': 89 })
        r2 = Rectangle(1, 1, 0, 0, 89)
        self.assertEqual(r1.id, r2.id)

    def create_rectangle2(self):
        """test method create new instance
        """
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        r2 = Rectangle(1, 1, 0, 0, 89)
        self.assertEqual(r1.width, r2.width)

    def create_rectangle3(self):
        """test method create new instance
        """
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        r2 = Rectangle(1, 2, 0, 0, 89)
        self.assertEqual(r1.width, r2.width)

    def create_rectangle4(self):
        """test method create new instance
        """
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        r2 = Rectangle(1, 2, 3, 0, 89)
        self.assertEqual(r1.id, r2.id)

    def create_rectangle4(self):
        """test method create new instance
        """
        r1 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        r2 = Rectangle(1, 2, 3, 4, 89)
        self.assertEqual(r1.id, r2.id)




if __name__ == "__main__":
    unittest.main()
