#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while my_list[i] and i <= x - 1:
            print("{}".format(my_list[i]), end="")
            i += 1
        print()
        return i
    except TypeError:
        print()
        return i
    except IndexError:
        print()
        return i
