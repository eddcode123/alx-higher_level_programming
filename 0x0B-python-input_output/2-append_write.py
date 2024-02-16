#!/usr/bin/pyhton3

""" defines a function that appends string to a textfile """


def append_write(filename="", text=""):
    """ append string to a file and return len(str) appended """
    # open file in append mode
    with open(filename, 'a', encoding='utf-8') as f:
        # append string
        f.write(text)
    return len(text)
