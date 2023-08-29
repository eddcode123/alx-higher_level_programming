#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # create a empty dict
    sorted_dict = {}

    # create a variables to store list keys
    mykeys = list(a_dictionary.keys())

    # sort list of keys
    mykeys.sort()
    # store sorted list of keys to sorted_dict
    sorted_dict = {i: a_dictionary[i] for i in mykeys}

    # print a_dictionary
    for k, v in sorted_dict.items():
        print("{}: {}".format(k, v))
