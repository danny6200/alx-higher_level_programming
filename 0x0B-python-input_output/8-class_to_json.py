#!/usr/bin/python3

"""
    This module supplies the class_to_json
    function
"""

import json


def class_to_json(obj):
    """
        This function converts a class object
        to a json format
    """
    if obj is None:
        return

    return obj.__dict__
