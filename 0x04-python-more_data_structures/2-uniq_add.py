#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return my_list
    uniq_list = set(my_list)
#    result = reduce(lambda x, y: x + y, uniq_list)
    result = 0
    for i in uniq_list:
        result += i
    return result
