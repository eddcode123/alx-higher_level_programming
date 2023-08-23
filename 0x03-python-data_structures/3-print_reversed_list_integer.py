#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if not my_list:
        pass
    else:
        # create a reversed copy of list
        reversed_list = my_list[::-1]
        # use for loop to print items of list
        for item in reversed_list:
            print("{:d}".format(item))
