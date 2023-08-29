#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create an empty list
    newlist = []
    # check if list is empty
    if (matrix):
        # assign squared values of list to newlist
        newlist = [item ** 2 if isinstance(item, int) else [value ** 2 for value in item] for item in matrix]

    return (newlist)
