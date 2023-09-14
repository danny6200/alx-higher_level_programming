#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0

    total = 0
    denom = 0
    for tup in my_list:
        total += (tup[0] * tup[1])
        denom += tup[1]
    average = total / denom
    return average
