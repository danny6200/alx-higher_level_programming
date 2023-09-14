#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    max_key = max(a_dictionary, key=lambda k: a_dictionary[k])
    return max_key
