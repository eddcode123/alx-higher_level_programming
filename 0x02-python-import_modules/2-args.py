#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    # Import the argv function from the sys module
    from sys import argv
    # Calculate the number of command-line arguments
    argslen = len(argv) - 1
    # Check the number of arguments and print number
    if argslen == 0:
        print("0 arguments.")
    elif argslen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argslen))
    # Iterate through the command-line arguments and print
    for i in range(1, argslen + 1):
        print("{}: {}".format(i, argv[i]))
