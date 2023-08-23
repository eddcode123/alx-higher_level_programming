#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argslen = len(argv) - 1
    if argslen == 0:
        print("{} arguments.".format(argslen))
    elif (argslen == 1):
        print("{} argument:".format(argslen))
        print("{}: {}".format(argslen, argv[argslen]))
    if argslen > 1:
        print("{} arguments:".format(argslen))
        for i in range(1, argslen):
            print("{}: {}".format(i, argv[i]))
