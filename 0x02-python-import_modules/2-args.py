#!/usr/bin/python3
from sys import argv
argslen = len(argv)
if (argslen == 1):
    print("{} arguments.".format(0))
else:
    if argslen != 1 and argslen > 1:
        print("{} arguments.".format(argslen - 1))
        for i in range(1, argslen):
            print("{}: {}".format(i, argv[i]))
