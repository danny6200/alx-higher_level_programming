#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif number < 0:
    pnum = -number
    ld = pnum % 10
    print(f"Last digit of {number} is -{ld} and is less than 6 and not 0")
else:
    ld = number % 10
    if ld > 5:
        print(f"Last digit of {number} is {ld} and is greater than 5")
    else:
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
