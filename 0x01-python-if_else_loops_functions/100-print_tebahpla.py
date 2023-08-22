#!/usr/bin/python3
# declare a variable to store first char
char = 122
length = 26

while char >= 97:
    if (length % 2 != 0):
        print("{:c}".format(char - 32), end="")
    else:
        print("{:c}".format(char), end="")
    length -= 1
    char -= 1
