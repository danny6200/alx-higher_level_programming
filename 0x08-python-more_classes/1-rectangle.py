#!/usr/bin/python3
"""
    This module provides the Rectangle Class

    Usage:
    ------
        >>> Rectangle = __import__('1-rectangle').Rectangle
        >>> my_rectangle = Rectangle()
"""


class Rectangle:
    """
        This class provides the blue print to
        create any Rectangular object.

        Attributes:
        -----------
            width (positive integer): private instance attribute
            height (positive integer): private instance attribute
        Methods:
        -------

    """
    def __init__(self, width=0, height=0):
        """
            This is the class contructor.

            It instantiates an object of this class
            and initializes the width and height
            attribute of an inatance of the class to
            the passed arguments.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            This is the getter method of the width attribute.

            It returns the width value of an inatance of the
            Rectangle class
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            This is the setter method of the width attribute.

            It sets the width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            This is the getter method of the height attribute.

            It returns the height value of an inatance of the
            Rectangle class
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            This is the setter method of the width attribute.

            It sets the width value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
