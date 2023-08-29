#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # check if key exist
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
