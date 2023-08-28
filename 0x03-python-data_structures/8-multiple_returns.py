#!/usr/bin/python3
def multiple_returns(sentence):
    # declare an empty tuple
    new_tuple = ()
    # check for a empty string
    if (sentence == ""):
        strlen = 0
        char = None
    else:
        strlen = len(sentence)
        char = sentence[0]
    new_tuple = (strlen, char)
    return (new_tuple)
