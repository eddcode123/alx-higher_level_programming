#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # create a new empty list
    new_list = []
    listlen = len(my_list)

    # check if idx is negative or out of bound
    if (my_list):
        if (idx < 0 or idx >= listlen):
            return (my_list)
        my_list.remove(my_list[idx])
        new_list = my_list

    return (new_list)
