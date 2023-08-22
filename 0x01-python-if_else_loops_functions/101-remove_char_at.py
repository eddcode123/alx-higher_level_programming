#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    if (n < 0):
        return str
    strlen = len(str)
    if (n > strlen):
        return str
    for i in range(strlen):
        if (i != n):
            newstr = newstr + str[i]
        i += 1
    return newstr
