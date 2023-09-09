#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    ln = len(my_list) - 1
    for i in range(ln, -1, -1):
        print(my_list[i])
