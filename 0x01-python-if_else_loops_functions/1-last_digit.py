#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# declare a varible last digit and store last digig of number
# deal with negative numbers
if (number < 0):
    lastdigit = number % -10
else:
    lastdigit = number % 10
# print out the last digit
print(f"Last digit of {number} is {lastdigit}", end=" ")
# check if the last digit is ! 0 and < 6
if (lastdigit == 0):
    print("and is 0")
elif (lastdigit > 5):
    print("and is greater than 5")
elif (lastdigit != 0 and lastdigit < 6):
    print("and is less than 6 and not 0")
