#!/usr/bin/python3
"""module with only one class, Square
"""
class Square:
    """class square with one function init
    """
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            print("size must be an integer")
            raise TypeError
        if (size < 0):
            print("size must be >= 0")
            raise ValueError
        self.__size = size
