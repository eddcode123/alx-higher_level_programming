#!/usr/bin/python3
def element_at(my_list, idx):
    # find length of list
    listlen = len(my_list)
    # check if idx is negative or greater than len of list
    if idx < 0 or idx >= listlen:
        return None
    return my_list[idx]
