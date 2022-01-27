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
        li3 = [4, 1, 2, 3]
        actual3 = max_integer(li3)
        self.assertEqual(4, actual3)
        li4 = [1, 2, 5, 3, 4]
        actual4 = max_integer(li4)
        self.assertEqual(5, actual4)
        li5 = [1, 2, -3, 4]
        actual5 = max_integer(li5)
        self.assertEqual(4, actual5)
        li6 = [-1, -2, -3, -4]
        actual6 = max_integer(li6)
        self.assertEqual(-1, actual6)
        li7 = [1]
        actual7 = max_integer(li7)
        self.assertEqual(1, actual7)
