#!/usr/bin/python3

"""
    This module supplies the add_item function
"""


import os
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """
        This function writes command
        line arguments in a list
        object and saves it in a
        json file
    """
    # Check if json file already exists
    if os.path.exists("add_item.json"):
        # Load list object from json file
        args_list = load_from_json_file("add_item.json")
    else:
        # Create an list
        args_list = []
    # Loop through the arguments
    # and append them to python object
    for arg in sys.argv[1:]:
        args_list.append(arg)

    # Save list to json file
    save_to_json_file(args_list, "add_item.json")


if __name__ == "__main__":
    main()
