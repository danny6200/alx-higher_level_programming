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
        --------
            area (integer): public instance method
            perimeter (integer): public instance method

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

    def area(self):
        """
            This method returns the area of a rectangle instance
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            This method returns the perimeter of a rectangle instance
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            This method returns the instance of the class in string format
        """
        result = ""
        if self.__width == 0 or self.__height == 0:
            result += "\n"
        else:
            for i in range(self.__height):
                result += "#" * self.__width + "\n"
        return result.rstrip()

    def __repr__(self):
        """
            This method returns the instance of the class in string format
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
            This method deletes an instance of the Rectangle class
        """
        print("Bye rectangle...")
