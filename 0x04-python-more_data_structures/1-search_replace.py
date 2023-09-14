#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return my_list
    return [replace if i == search else i for i in my_list]


"""
    new_list = my_list[:]
    for i in new_list:
        if i == search:
            i = replace
"""
