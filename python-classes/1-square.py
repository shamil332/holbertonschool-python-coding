#!/usr/bin/python3
""" this module is for the class Square"""
class Square:
    """this square define a size"""
    def __init__(self, size=0):
        """initializes a size which must be an integer and =>"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
