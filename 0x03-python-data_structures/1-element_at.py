#!/usr/bin/python3
def element_at(my_list, idx):
    # find length of list
    listlen = len(my_list)
    # check if a negative index is passed
    if idx < 0:
        return None
    elif idx > listlen:
        return None
    else:
        return my_list[idx]
