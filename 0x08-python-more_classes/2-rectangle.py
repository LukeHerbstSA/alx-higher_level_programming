#!/usr/bin/python3

"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    @staticmethod
    def heightcheck(height):
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")

    @staticmethod
    def widthcheck(width):
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")

    def __init__(self, width=0, height=0):
        Rectangle.heightcheck(height)
        Rectangle.widthcheck(width)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * self.__width + 2 * self.__height)

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        Rectangle.heightcheck(height)
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        Rectangle.widthcheck(width)
        self.__width = width
