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

    def __str__(self):
        """
            This method returns a string
            representation of a rectangle instance
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
            This method returns the area of a rectangle instance
        """
        return self.__width * self.__height
