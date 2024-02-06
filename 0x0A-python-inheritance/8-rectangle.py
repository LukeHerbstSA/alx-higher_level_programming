#!/usr/bin/python3
"""
Rectangle modules - imports BaseGeomtry to inherit
"""


class BaseGeometry:
    """
    initializes passed name and value, based on measurements
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value < 1):
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Rectangle class - initializes Rectangle instances
    """
    def __init__(self, width, height):
        self.integer_validator("", width)
        self.integer_validator("", height)
        self.__width = width
        self.__height = height
