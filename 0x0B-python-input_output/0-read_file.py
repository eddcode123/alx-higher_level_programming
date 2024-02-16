#!/usr/bin/python3

""" defines function that reads a text file"""


def read_file(filename=""):
    # Open filename in read mode ('r') with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as f:
        # Read and Print file contents to STDOUT
        print(f.read(), end='')
