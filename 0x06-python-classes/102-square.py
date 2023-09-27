#!/usr/bin/python3

'''This is amodule-level docstring'''


class Square:
    '''This is a docstring for the Square class.

    This docstring provides an overview of what
    the class does and any important information
    about its usage, attributes, and methods.

    Attributes:
        __size (number): Description of attribute1.
        attribute2 (type): Description of attribute2.

    Methods:
        method1(args): Description of method1.
        method2(args): Description of method2.
    '''

    def __init__(self, size=0):
        '''This is the constructor of the Square class

        It instantiates an object of the Square class
        with an attribute of size
        '''
        self.__size = size

    @property
    def size(self):
        '''This is a property getter function for the

        the private instance attribute size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''This is a property setter function for the

        the private instance attribute size.

        It validates and sets the value of size
        '''
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''This is a docstring for the area method

        It computes the area of a square of the given size
        '''
        return self.__size ** 2

    def __eq__(self, other):
        '''
        This is used to check the eqaulity of
        two square instances
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        '''
        This checks if two square instances are unequal
        '''
        return self.area() != other.area()

    def __gt__(self, other):
        '''
        This checks if one square instance
        is greater than the other
        '''
        return self.area() > other.area()

    def __ge__(self, other):
        '''
        This checks if the self square instance
        is greater than or equal to the other
        square instance
        '''
        return self.area() >= other.area()

    def __lt__(self, other):
        '''
        This checks if the self square instance is
        is less than the other square instance
        '''
        return self.area() < other.area()

    def __le__(self, other):
        '''
        This checks if the self square instance
        is less than or equal to the other square
        instance
        '''
        return self.area() <= other.area()
