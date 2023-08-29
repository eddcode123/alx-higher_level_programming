#!/usr/bin/python3
def uniq_add(my_list=[]):
    # create a set to store unique values
    uniquevalues = set()

    # use a nested loop to iterate and pick unique elements
    if (my_list):
        for item in my_list:
            # add values to uniquevalues
            uniquevalues.add(item)

        # use sum to add elements of set
        add = sum(uniquevalues)

    return (add)
