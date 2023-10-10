#!/usr/bin/python3

"""
    This module supplies the to_json_string
    function
"""


import json

def to_json_string(my_obj):
    """
        This function converts an object
        to a JSON string/format
    """
    if my_obj is None:
        return

    # json_string = json.dumps(my_obj)

    return json.dumps(my_obj)
