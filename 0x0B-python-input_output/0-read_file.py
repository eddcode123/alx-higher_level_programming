#!/usr/bin/python3

def read_file(filename=""):
    # Open filename in read mode ('r') with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as f:
        # Read file contents and store it in 'data'
        data = f.read()
    # Print file contents to STDOUT
    print(data)
