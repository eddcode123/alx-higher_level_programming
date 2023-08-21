#!/usr/bin/python3
num = 0
while num < 100:
    if (num <= 98):
        print("{:02}".format(num), end=", ")
    elif (num == 99):
        print("{}".format(num))
    num += 1
