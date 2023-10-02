#!/usr/bin/python3
"""
    This module supplies the print_square function

    Usage:
    ------
        >>> print_square = __import__('4-print_square').print_square
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
"""


def print_square(size):
    """
        This function prints a square of length size

        Argument:
        ---------
            size (integer)

        Return Value:
        -------------
            It returns no value
    """
    if size is None:
        raise TypeError
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
