#!/usr/bin/python3
def safe_print_integer(value):
    # print value passed to function
    # use try and except
    try:
        # if value is integer print value and return true
        print("{:d}".format(value))
        return (True)
    except Exception:
        # return false if exception is encountered
        return (False)
