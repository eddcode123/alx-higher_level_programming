#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    # Initialize sum with value of zero
    sum = 0
    # calculate len of argv - 1to exclude program name
    argslen = len(argv) - 1
    # use a for loop to iterate and calculate sum
    for i in range(1, argslen + 1):
        # check if the user didnt pass arguments
        if argslen == 1:
            sum = 0
        else:
            # type cast and add argv at index i
            sum += int(argv[i])
    print("{}".format(sum))
