#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
        This function checks if an instance
        or object of a class belongs to that
        class
    """
    if obj is None or a_class is None:
        return
    if not isinstance(obj, a_class):
        return False
    return True
