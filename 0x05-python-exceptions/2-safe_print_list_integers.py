#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # create a count variable to return elements printed
    count = 0

    # print all element of list in a single line
    if (my_list):
        for i in range(x):
            # use try and except
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                pass
            except TypeError:
                pass
            else:
                count += 1
    print()
    return (count)
