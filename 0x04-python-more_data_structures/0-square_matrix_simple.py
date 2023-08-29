#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create a copy of matrix
    newmatrix = matrix.copy()

    # iterlate the newmatrix and square its values
    for i in range(len(matrix)):
        newmatrix[i] = list(map(lambda item: item ** 2, matrix[i]))

    return (newmatrix)
