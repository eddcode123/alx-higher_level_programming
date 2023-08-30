#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # create a list to store keys to delete
    keys_to_delete = []

    # iterate through dictionary
    if (a_dictionary):
        for k, v in a_dictionary.items():
            if v == value:
                # add keys to my keys list
                keys_to_delete.append(k)
    # delete all keys in list
    for key in keys_to_delete:
        del a_dictionary[key]

    return (a_dictionary)
