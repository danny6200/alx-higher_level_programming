#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    new_dict = dict()
    for key, value in a_dictionary.items():
        new_dict[key] = 2 * value
    return new_dict
