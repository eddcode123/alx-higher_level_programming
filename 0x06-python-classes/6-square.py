#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0,  position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size of size instance in class square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set value of size instance in class square."""
        if not isinstance(value, int):
            # raise a type error exception
            raise TypeError("size must be an integer")
        elif (value < 0):
            # raise value error exception
            raise ValueError("size must be >= 0")
        # update size
        self.__size = value

    @property
    def position(self):
        """Get position value ."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of a square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the squre ro stdout or a newline if size is zero."""
        # if size is zero and print empty line
        if (self.__size == 0):
            print()
        else:
            # print square
            for i in range(self.position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print()
