#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = None
    # check is set is not empty
    if (set_1 and set_2):
        common = set_1 & set_2

    return (common)
