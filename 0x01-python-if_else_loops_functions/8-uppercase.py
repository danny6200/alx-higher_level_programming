#!/usr/bin/python3
def uppercase(str):
    ln = len(str)
    for i, c in enumerate(str):
        if c >= chr(97) and c <= chr(122):
            print("{}".format(chr(ord(c) - 32)), end="" if i < ln-1 else "\n")
        else:
            print("{}".format(c), end="" if i < ln - 1 else "\n")
