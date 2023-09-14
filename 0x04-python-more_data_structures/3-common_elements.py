#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None:
        return set_1
    if set_2 is None:
        return set_2
    comm_elements = set_1.intersection(set_2)
    return comm_elements
