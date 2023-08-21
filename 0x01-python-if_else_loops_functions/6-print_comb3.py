#!/usr/bin/python3
# declare two varibles x and y
x = 0
# use a while loop to iterate and combine x and y
while x < 10:
    y = x + 1
    while y < 10:
        if (x != y) and x < 8:
            print("{}{}".format(x, y), end=", ")
        else:
            print("{}{}".format(x, y))
        y += 1
    x += 1
