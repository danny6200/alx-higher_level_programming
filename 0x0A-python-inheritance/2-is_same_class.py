#!/usr/bin/python3
def is_same_class(obj, a_class):
    if obj is None or a_class is None:
        return
    if not isinstance(obj, a_class):
        return False
    return True
