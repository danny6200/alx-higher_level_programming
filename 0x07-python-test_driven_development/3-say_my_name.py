#!/usr/bin/python3
"""
    This module supplies the say_my_name function

    Usage:
    ------
        >>> say_my_name = __import__('3-say_my_name').say_my_name
        >>> say_my_name("Bob", "White")
        Bob White
"""


def say_my_name(first_name, last_name=""):
    """
        This function prints the first and last name of a person

        Arguments:
        ----------
            first_name (string): first argument
            last_name (string): second argument

        Return Value:
        -------------
            It returns no value
    """
    # Check if first_name is None
    if first_name is None:
        raise TypeError
    # Check if first_name is NOT a string type
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if last_name is NOT a string type
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
