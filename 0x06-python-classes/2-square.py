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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
