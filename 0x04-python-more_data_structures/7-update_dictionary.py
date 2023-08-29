#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # iterate dict
    for k, v in a_dictionary.items():
        # check if key exist
        if (k == key):
            a_dictionary[k] = value # update value at key
        else:
            a_dictionary[k] = value
