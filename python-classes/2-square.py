#!/usr/bin/python3
"""A module for the class Square"""


class Square:
    """a class that defines a square with a size"""
    def __init__(self, size=0):
        """initializes a size that must be an integer and must be >= 0"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """this func finds area of the square"""
        return self.__size**2
