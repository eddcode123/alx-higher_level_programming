#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    # declare len of argv
    argslen = len(argv) - 1
    # check if len of arguments is 3
    if argslen != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    # assign value to respective varibles
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    # check if op matches if not print the message
    if op not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    # declare a varible result to store result & initialize to none
    result = None
    # check if the conditions are met
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    # print result
    print("{} {} {} = {}".format(a, op, b, result))
