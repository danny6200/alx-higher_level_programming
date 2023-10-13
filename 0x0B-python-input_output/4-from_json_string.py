#!/usr/bin/python3

"""
    This module supplies the from_json_string
    function
"""


import json


def from_json_string(my_str):
    """
        This function converts a json_string
        to a python object
    """
    if my_str is None:
        return

    return json.loads(my_str)
