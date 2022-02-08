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

    def test_id2(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id3(self):
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_to_string(self):
        """test method for to_string of base
        """
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string([ { 'id': 12 }])        
        self.assertEqual(json_dictionary, "[{"id": 12}]")

    def test_from_jason_string(self):
        """test method from_json_string of base
        """
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])
        list_output = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(list_output, [{'id': 89}])
        list_output = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(list_output, [{'id': 89}])

if __name__ == "__main__":
    unittest.main()
