#!/usr/bin/python3

"""
    This module supplies lookup function

    It is used to loop up the methods
    and attributes of an object
"""


def lookup(obj):
    """
        This function list the attributes and
        methods of object passed to it.
    """
    if obj is None:
        return
    return dir(obj)
