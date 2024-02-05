#!/usr/bin/python3
"""
class basegeometry, contains geometric based methods
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
