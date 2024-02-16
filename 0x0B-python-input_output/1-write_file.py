#!/usr/bin/python3

""" difines a function that writes to a file """


def write_file(filename="", text=""):
    """ writes a str to file and returns length of str"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
