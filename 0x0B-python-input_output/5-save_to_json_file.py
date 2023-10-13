#!/usr/bin/python3

"""
    This module supplies the save_to_json_file
    function
"""

import json


def save_to_json_file(my_obj, filename):
    """
        This function saves an object in JSON
        format in a file
    """
    if filename is None or my_obj is None:
        return

    # json_string = json.dumps(my_obj)

    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
