#!/usr/bin/python3
def weight_average(my_list=[]):
    mul = 0
    div = 0

    # check if list is empty
    if not my_list:
        return (0)
    for item in my_list:
        mul += item[0] * item[1]
        div = item[1]

    return (mul / div)
