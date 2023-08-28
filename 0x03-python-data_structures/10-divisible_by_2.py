#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # create an empty list
    new_list = []

    # check for empty list
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)

    return (new_list)
