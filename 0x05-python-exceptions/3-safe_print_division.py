#!/usr/bin/python3
def safe_print_division(a, b):
    # create a result varibale
    result = 0

    # divide a and b in try clause
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return (result)
