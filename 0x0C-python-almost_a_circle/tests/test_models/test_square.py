#!/usr/bin/python3
""" Unittest of Square class"""
import io
import sys
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test of class Square """

    def test_init_square(self):
        """test method for initialisation of square
        """
        s = Square(1)
        s2 = Square(1, 2)
        self.assertEqual(s.size, s2.size)

    def test_init_square2(self):
        """test method for initialisation of square
        """
        s = Square(1, 2)
        s2 = Square(1, 2, 3)
        self.assertEqual(s.x, s2.x)

    def test_init_square3(self):
        """test method for initialisation of square
        """
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)
 
    def test_init_square4(self):
        """test method for initialisation of square
        """
        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s2.id, 4)

    def test_init_squaree_type_error(self):
        """test method for check type error case of square
        """
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_init_square_value_error(self):
        """test method for check value error case of square
        """
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        """test method for the calculation of area
        """
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

    def test_update(self):
        """test method update the instance by args
        """
        r1 = Rectangle(2, 3, 4, 5, 1)
        r1.update()
        r2 = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(r1.y, r2.y)

    def test_update_by_args(self):
        """test method update the instance by args
        """
        s1 = Square(10, 10, 10, 10)
        s1.update()
        s2 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, s2.width)

    def test_update_by_args2(self):
        """test method update the instance by args
        """
        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.id, 89)

    def test_update_by_args3(self):
        """test method update the instance by args
        """
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 1)
        self.assertEqual(s1.size, 1)

    def test_update_by_args4(self):
        """test method update the instance by args
        """
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 1, 2)
        self.assertEqual(s1.x, 2)

    def test_update_by_args5(self):
        """test method update the instance by args
        """
        s1 = Square(10, 10, 10, 10)
        s1.update(89, 1, 2, 3)
        self.assertEqual(s1.y, 3)

    def test_update_by_kwargs(self):
        """test method update the instance by **kwargs
       	"""
        s1 = Square(10, 10, 10, 10)
        s1.update(**{ 'id': 89 })
        self.assertEqual(s1.id, 89)

    def test_update_by_kwargs2(self):
        """test method update the instance by **kwargs
       	"""
        s1 = Square(10, 10, 10, 10)
        s1.update(**{ 'id': 89, 'size': 1 })
        self.assertEqual(s1.size, 1)

    def test_update_by_kwargs3(self):
        """test method update the instance by **kwargs
       	"""
        s1 = Square(10, 10, 10, 10)
        s1.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s1.x, 2)

    def test_update_by_kwargs4(self):
        """test method update the instance by **kwargs
       	"""
        s1 = Square(10, 10, 10, 10)
        s1.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        self.assertEqual(s1.y, 3)

    def test_string(self):
        """test method check __str()__
       	"""
        s1 = Square(4, 6, 2, 1)
        strr = s1.__str__()
        strrr = "[Square] (1) 6/2 - 4"
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

    def test_create_rectangle(self):
        """test method create new instance
        """
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)

    def test_create_rectangle2(self):
        """test method create new instance
        """
        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.size, 1)

    def test_create_rectangle3(self):
        """test method create new instance
        """
        s1 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        self.assertEqual(s1.x, 2)

    def test_create_rectangle4(self):
        """test method create new instance
        """
        s1 = Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })
        s2 = Square(1, 2, 3, 89)
        sd = s2.to_dictionary()
        ss = Square.create(**sd)
        self.assertEqual(s1.id, ss.id)

    def test_save_to_file(self):
        """test method save to file
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            f = file.read()
        self.assertEqual(f, "[]")

    def test_save_to_file2(self):
        """test method save to file
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            f = file.read()
        self.assertEqual(f, "[]")

    def test_save_to_file3(self):
        """test method save to file
        """
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as file:
            f = file.read()
        self.assertEqual(f[0:9], "[{\"x\": 0,")

    def test_load_from_file(self):
        """test method load a file
        """
        with self.assertRaises(NameError):
            r = Rectange.load_from_file()

    def test_load_from_file2(self):
        """test method load a file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0])[-10:], "2/8 - 10/7")

if __name__ == "__main__":
    unittest.main()
