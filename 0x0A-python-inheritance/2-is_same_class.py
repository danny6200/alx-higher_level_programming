#!/usr/bin/python3
"""
    This module supplies the is_same_class
    function.
"""


def is_same_class(obj, a_class):
    """
        This function checks if an instance
        or object of a class belongs to that
        class
    """
    if obj is None:
        return
    if not isinstance(obj, a_class):
        return False
    return True
