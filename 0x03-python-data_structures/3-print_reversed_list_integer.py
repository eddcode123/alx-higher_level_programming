#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # use reverse function to reverse list
    my_list.reverse()
    # use for loop to print items of list
    for item in my_list:
        print("{:d}".format(item))
