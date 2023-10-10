#!/usr/bin/python3

"""
    This module supplies the load_from_json_file
    function
"""


import json


def load_from_json_file(filename):
    """
        This function loads object from
        a json file
    """
    # Check if filename is passed
    if filename is None:
        return

    # Open file
    with open(filename, "r") as file:
        # Read file content
        content = file.read()

    # Convert content to python object
    # Return object
    return json.loads(content)
