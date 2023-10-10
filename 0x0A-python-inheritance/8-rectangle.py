#!/usr/bin/python3

"""
    This module supplies the Rectangle class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
        This class inherits the methods and
        attributes of the BaseGeometry class
    """
    def __init__(self, width, height):
        """
            This is the class constructor
        """
        self.__width = 0
        self.__height = 0
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
