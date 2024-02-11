#!/usr/bin/python3
"""
Square subclass of Rectangle
"""
Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    """
    class square uses inheritance to initialize special isntances
    """
    def __str__(self):
        out = "[Rectangle] ({}) {}/{} {}/{}".format(id, self.__width, self.__height, self.x, self.y)
        return (out)

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x, y, id)

    def update(self, *args, **kwargs):


    @property
    def size(self):
        return (self.width)

    @property.setter
    def size(self, value):
        super().integer_validator("width", value)
        self.__width = value
        self.__height = value
