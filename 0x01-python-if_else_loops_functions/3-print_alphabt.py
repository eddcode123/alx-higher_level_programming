#!/usr/bin/python3
# declare a varible character to store ascii code for lowercase a
char = 97
# use a while loop to iterate through code
# use if statment to remove q and e
while char < 123:
    if (char != ord("q") and char != ord("e")):
        print("{}".format(chr(char)), end="")
    char += 1
