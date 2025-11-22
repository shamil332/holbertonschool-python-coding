#!/usr/bin/python3
"""A module for the class Square"""


class Square:
    """a class that defines a square with a size"""
    def __init__(self, size=0):
        """Initialize a new Square."""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """this func finds area of the square"""
        return self.__size**2
