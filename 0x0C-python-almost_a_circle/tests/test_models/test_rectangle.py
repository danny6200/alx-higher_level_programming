#!/usr/bin/python3

"""
    This is a test file for rectangle class.
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """
        This is the test case for the base class
    """
    def setUp(self):
        print("setUp")
        self.r_1 = Rectangle(10, 2)
        self.r_2 = Rectangle(2, 10)
        self.r_3 = Rectangle(10, 2, 0, 0, 12)
        self.r_4 = Rectangle(10, 2, 2, 0, 10)

    def test_default_rect_id_from_base(self):
        self.assertEqual(self.r_1.id, 1)

    def test_default_rect_id_from_base(self):
        self.assertEqual(self.r_2.id, 2)

    def test_custom_rect_id(self):
        self.assertEqual(self.r_3.id, 12)

    def test_rect_width_value_validation(self):
        with self.assertRaises(ValueError):
            self.r_1.width = -2
    
    def test_rect_width_type_validation(self):
        with self.assertRaises(TypeError):
            self.r_1.width = "School"

    def test_rect_height_value_validation(self):
        with self.assertRaises(ValueError):
            self.r_2.height = -1

    def test_rect_height_type_validation(self):
        with self.assertRaises(TypeError):
            self.r_2.height = "14"

    def test_rect_xcoord_value_validation(self):
        with self.assertRaises(ValueError):
            self.r_3.x = -20

    def test_rect_xcoord_type_validation(self):
        with self.assertRaises(TypeError):
            self.r_3.x = 23.98
    
    def test_rect_ycoord_value_validation(self):
        with self.assertRaises(ValueError):
            self.r_3.y = -23

    def test_rect_ycoord_type_validation(self):
        with self.assertRaises(TypeError):
            self.r_3.y = "12"

    def test_rect_area(self):
        self.assertEqual(self.r_1.area, 20)
    
    # def test_rect_display_v1(self):
    #     self.assertEqual(self.r_1.display(), "##########\n##########")

    def test_rect_string_rep(self):
        self.assertEqual(print(self.r_3), "[Rectangle] (12) 0/0 - 10/2")

    def test_rect_display(self):
        self.assertEqual(self.r_4.display(), "  ##########\n  ##########")

    def tearDown(self):
        print("tearDown")
        del self.r_1
        del self.r_2
        del self.r_3
        del self.r_4

if __name__ == "__main__":
    unittest.main()
