#!/usr/bin/python3
"""
    This module supplies the add_integer function.

    Usage:
    -----
        >>> from add_integer import add_integer

        >>> print(add_integer(12, 34)
        56
"""

def add_integer(a, b=98):
    """
        This function returns the sum of two integers

        Arguments:
        ---------
            a (integer/float): first argument
            b (integer/float): second argument

        Return Value:
        ------------
        a + b (integer)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
