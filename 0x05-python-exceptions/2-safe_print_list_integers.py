#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                item = my_list[i]
                print("{:d}".format(item), end="")
                count += 1
            except (ValueError, TypeError):
                pass
        print()
        return count
    except TypeError as e:
        print("IndexError: {}".format(e))
