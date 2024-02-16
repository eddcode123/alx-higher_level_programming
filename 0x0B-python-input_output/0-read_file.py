#!/usr/bin/python3

""" defines function that reads a text file"""


def read_file(filename=""):
    """Print the contests of a UTF8 text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        # Read and Print file contents to STDOUT
        print(f.read(), end='')
