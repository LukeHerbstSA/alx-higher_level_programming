#!/usr/bin/python3
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator("", width)
        BaseGeometry.integer_validator("", height)
        self.__width = width
        self.__height = height
