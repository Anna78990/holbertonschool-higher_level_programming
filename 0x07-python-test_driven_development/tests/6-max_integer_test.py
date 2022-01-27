#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        li = []
        actual = max_integer(li)
        expected = None
        self.assertEqual(expected, actual)
        li2 = [1, 2, 3, 4]
        actual2 = max_integer(li2)
        self.assertEqual(4, actual2)
