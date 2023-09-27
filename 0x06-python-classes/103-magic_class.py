#!/usr/bin/python3
'''
This module contains the Circle class
its attributes and methods
'''

import math


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
        '''
        This is the circle class contructor

        '''
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''
        This returns the area of the circle
        '''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''
        This returns the circumference of the circle
        '''
        return 2 * math.pi * self.__radius
