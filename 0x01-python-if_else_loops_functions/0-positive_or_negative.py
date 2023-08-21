#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# use if elif and else to test each condition
if (number > 0):
    print(f"{number} is positive")
elif (number < 0):
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
