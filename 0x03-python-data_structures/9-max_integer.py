#!/usr/bin/python3
def max_integer(my_list=[]):
    # check if list is empty
    if not my_list:
        return None
    # initianilize maxvaslue with address of 1st item of list
    maxvalue = my_list[0]

    # iterate through list to find maxvalue
    for item in my_list:
        if item > maxvalue:
            maxvalue = item

    return maxvalue
