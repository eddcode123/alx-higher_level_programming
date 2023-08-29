#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # check if key exist
    if key in a_dictionary:
        a_dictionary[key] = value # update value at key
    else:
        a_dictionary[key] = value # add key - value pair
    return (a_dictionary)
