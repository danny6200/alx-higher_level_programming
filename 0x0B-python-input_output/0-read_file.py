#!/usr/bin/python3
"""
    This module supplies the read_file function
"""


def read_file(filename=""):
    """
        This function reads the content of a file
        and prints them to standard output
    """
    if filename is None:
        return

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    print(content.rstrip())
