#!/usr/bin/python3
num = 0
while num < 100:
    print("{:02}".format(num), end=", ")
    if (num == 99):
        print("{}".format(num))
    num += 1
