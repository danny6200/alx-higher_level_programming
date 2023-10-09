#!/usr/bin/python3
"""
    This module supplies the is_kind_of_class
    method
"""


def is_kind_of_class(obj, a_class):
    """
        This function returns True
        if obj is an instance/object
        of a_class or instance/object
        of a subclass of a_class

        It returns False if otherwise
    """
    if obj is None:
        return
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False
