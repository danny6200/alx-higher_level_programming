#!/usr/bin/python3

"""
    This script reads input from stdin
    and compute some metrics based off
    the input
"""


import sys
import os


def main():
    """
        This function holds the logic
        for reading from input and
        computing the required metrics
    """
    try:
        File_size = 0
        status_codes = dict()
        line_buffer = []

        for line in sys.stdin:

            line_file_size = line.split()[-1]
            File_size += int(line_file_size)
            status_code = line.split()[-2]

            if status_code in status_codes.keys():
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

            line_buffer.append(line)

            if len(line_buffer) == 10:
                print("File size: {:d}".format(File_size))
                for key, value in status_codes.items():
                    print("{}: {:d}".format(key, value))
                print()
                
                File_size = 0
                status_codes = dict()
                line_buffer = []

    except KeyboardInterrupt as e:
        print(e)

if __name__ == "__main__":
    main()
