#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if (not isinstance(size, int)):
            print("size must be an integer")
            raise TypeError
        if (size < 0):
            print("size must be >= 0")
            raise ValueError
        self.__size = size
    def area(self):
        return (self.__size * self.__size)
    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            print("size must be an integer")
            raise TypeError
        if (size < 0):
            print("size must be >= 0")
            raise ValueError
        self.__size = size
