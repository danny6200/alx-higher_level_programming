#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ln = len(sys.argv)
    sum = 0
    if ln == 1:
        print(sum)
    else:
        for i in range(1, ln):
            sum += int(sys.argv[i])
        print(sum)
