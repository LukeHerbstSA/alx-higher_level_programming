#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    pedantic pedantic pedantic documentation
    """
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
