#!/usr/bin/python3
import math


'''
This module contains the Circle class
its attributes and methods
'''


class MagicClass:
    '''
    This is a Circle class

    Attributes:
    ----------
        radius(number): defines the radius of a circle

    Methods:
    -------
        area(number): returns the value of the area of a circle
        circumference(number): returns the value of
        the circumference of a circle
    '''

    def __init__(self, radius):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
