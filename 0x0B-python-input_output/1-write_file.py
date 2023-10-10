#!/usr/bin/python3

"""
    This module supplies the write_file function
"""


def write_file(filename="", text=""):
    """
        This function writes a text string (UTF8)
        to a file
    """
    if filename is None:
        return

    with open(filename, "w") as file:
        num_chars = file.write(text)

    return num_chars
