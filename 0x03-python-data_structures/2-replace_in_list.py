#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # find length of list
    listlen = len(my_list)
    # check if idx is negative and is out of bound
    if (idx < 0 or idx >= listlen):
        return my_list
    my_list[idx] = element
    return my_list
