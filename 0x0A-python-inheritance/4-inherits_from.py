#!/usr/bin/python3

"""
    This module supplies the inherits_from
    function
"""


def inherits_from(obj, a_class):
    """
        This function returns True
        if and only if obj's class
        inherits from a_class
    """
    if obj is None:
        return
    if issubclass(type(obj), a_class):
        return True
    return False
