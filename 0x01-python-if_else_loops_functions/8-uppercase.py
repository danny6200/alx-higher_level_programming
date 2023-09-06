#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print(" ")
    for i, c in enumerate(str):
        if c >= chr(97) and c <= chr(122):
            print("{}".format(chr(ord(c) - 32)), end="" if i < len(str) - 1 else "\n")
        else:
            print("{}".format(c), end="" if i < len(str) - 1else "\n")
