#!/usr/bin/python3
from 7-base_geometry import BaseGeometry
"""
Rectangle modules - imports BaseGeomtry to inherit
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class - initializes Rectangle instances
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator("", width)
        BaseGeometry.integer_validator("", height)
        self.__width = width
        self.__height = height
