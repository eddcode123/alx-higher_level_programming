#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # create a new dict
    newdict = {}

    # iterate and assigned new values to newdict
    if (a_dictionary):
        for k, v in a_dictionary.items():
            newdict[k] = v * 2
    return (newdict)
