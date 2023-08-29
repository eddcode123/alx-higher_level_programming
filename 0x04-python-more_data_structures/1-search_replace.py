#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # create emptylist
    newlist = []

    # iterate list if not empty and check and replace element
    if (my_list):
        for item in my_list:
            # check if search is in the list
            if (item == search):
                newlist.append(replace)
            else:
                newlist.append(item)

    return (newlist)
