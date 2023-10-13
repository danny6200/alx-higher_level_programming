#!/usr/bin/python3

"""
    This module supplies the append_after
    function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
        This function appends some string after
        a particular string
    """
    if filename is None or search_string is None:
        return

    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
