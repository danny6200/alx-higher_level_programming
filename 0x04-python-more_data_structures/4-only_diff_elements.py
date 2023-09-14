#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None:
        return set_1
    if set_2 is None:
        return set_2
    s12 = set_1.difference(set_2)
    s21 = set_2.difference(set_1)
    od_set = s12.union(s21)
    return od_set
