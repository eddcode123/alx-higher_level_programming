#!/usr/bin/python

def read_file(filename=""):
    # Open the file specified by filename in read mode ('r') with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as f:
        # Read the contents of the file and store it in the variable 'data'
        data = f.read()
    # Print the contents of the file to the console
    print(data)
