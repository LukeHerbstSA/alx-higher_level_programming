#!/usr/bin/python3
"""
Rectangle modules - imports BaseGeomtry to inherit
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class - initializes Rectangle instances
    """
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)
