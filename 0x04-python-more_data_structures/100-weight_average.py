#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    num1 = 0

    # check if list is empty
    if not my_list:
        return (0)
    for item in my_list:
        num += item[0] * item[1]
        num1 += item[1]

    return (num / num1)
