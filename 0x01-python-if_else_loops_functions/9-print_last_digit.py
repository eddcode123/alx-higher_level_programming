#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = 0
    if number < 0:
        lastdigit = (number * -1) % 10
    else:
        lastdigit = number % 10
    print("{}".format(lastdigit), end="")

    return (lastdigit)
