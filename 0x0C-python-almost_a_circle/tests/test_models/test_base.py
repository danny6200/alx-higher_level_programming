#!/usr/bin/python3

"""
    This is a test file for the base class.
"""


import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """
        This is the test case for the base class
    """
    def setUp(self):
        print("setUp")
        self.b_1 = Base()
        self.b_2 = Base(15)
        self.b_3 = Base()
        self.b_4 = Base()

    def test_default_base_id(self):
        self.assertEqual(self.b_1.id, 1)

    def test_custom_base_id(self):
        self.assertEqual(self.b_2.id, 15)

    def test_second_default_base_id(self):
        self.assertEqual(self.b_3.id, 2)

    def test_third_default_base_id(self):
        self.assertEqual(self.b_4.id, 3)

    def tearDown(self):
        print("tearDown")
        del self.b_1
        del self.b_2
        del self.b_3
        del self.b_4


if __name__ == '__main__':
    unittest.main()
