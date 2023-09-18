#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """represent a Rectangle."""
    def __init__(self, width=0, height=0):
        """initializing a rectangle

        Args:
            width (int): width of a rectangle.
            height(int): height of a rectamgle.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """Get height of private instance"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set value to private instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get  width of private instance"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set value to private instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
