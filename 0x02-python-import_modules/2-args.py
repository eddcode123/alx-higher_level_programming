#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argslen = len(argv) - 1
    if argslen == 0:
        print("0 arguments.")
    elif argslen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argslen))
    for i in range(1, argslen + 1):
        print("{}: {}".format(i, argv[i]))
