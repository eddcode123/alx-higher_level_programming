#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # find length of list
    listlen = len(my_list)
    my_listcopy = my_list.copy()
    if (idx < 0 or idx >= listlen):
        return my_listcopy
    my_listcopy[idx] = element
    return my_listcopy
