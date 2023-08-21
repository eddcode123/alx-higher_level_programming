#!/usr/bin/python3
# create a function islower
def islower(c):
    char = 97
    while 97 < 123:
        if (ord(c) == char):
            return True
        else:
            return False
        char += 1
