#!/usr/bin/python3

"""
    This module supplies the append_write function
"""


def append_write(filename="", text=""):
    """
        This function appends a text string
        to the end of a file
    """
    if filename is None:
        return

    with open(filename, "a") as file:
        num_chars = file.write(text)

    return num_chars
