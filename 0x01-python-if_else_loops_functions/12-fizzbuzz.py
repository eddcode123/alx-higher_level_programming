#!/usr/bin/python3
# define function method
def fizzbuzz():
    # use a for loop to iterate from 0 ro 100
    for i in range(1, 101):
        # check for numbers divisible by 3
        if (i % 3 == 0 and i % 5 == 0):
            print("{}".format("FizzBuzz"), end=" ")
        elif (i % 5 == 0):
            print("{}".format("Buzz"), end=" ")
        elif (i % 3 == 0):
            print("{}".format("Fizz"), end=" ")
        else:
            print("{}".format(i), end=" ")
