#!/usr/bin/python3
def no_c(my_string):
    ln = len(my_string)
    for i, c in enumerate(my_string):
        if c == 'c' or c == 'C':
            continue
        print("{}".format(c), end="" if i < ln - 1 else "\n") 
