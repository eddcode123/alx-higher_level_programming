#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        @property
        def size(self):
            """Get/set cuurent size of square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        
        def area(self):
            """return  area of the square."""
            self.area = (self.__size * self.__size)
            return (self.area)
