#!/usr/bin/python3
"""
module rectangle
"""
Base = __import__("base").Base


class Rectangle(Base):
    """
    class Rectangle - inherits from rectangle
    """
    def __str__(self):
        firsthlf = "[Rectangle] ({}) {}/{} ".format(self.id, self.x, self.y)
        scndhlf = "- {}/{}".format(self.width, self.height)
        return (firsthlf + scndhlf)

    @staticmethod
    def validator(*values):
        for i in range(0, len(values)):
            if ((i % 2) != 0):
                attr = values[i - 1]
                if (not isinstance(values[i], int)):
                    raise TypeError("{} must be an integer".format(attr))
                if (values[i] <= 0 and (attr == "width" or attr == "height")):
                    raise ValueError("{} must be > 0".format(attr))
                if (values[i] < 0 and (attr == "x" or attr == "y")):
                    raise ValueError("{} must be >= 0".format(attr))

    def __init__(self, width, height, x=0, y=0, id=None):
        Rectangle.validator(["width", width, "height", height, "x", x, "y", y])
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def update(self, *args, **kwargs):
        if (args is None):
            for key, value in kwargs:
                setattr(self, key, value)
            return
        for i in range(0, len(args)):
            if (i == 0):
                self.id = args[i]
            if (i == 1):
                self.__width = args[i]
            if (i == 2):
                self.__height = args[i]
            if (i == 3):
                self.x = args[i]
            if (i == 4):
                self.y = args[i]

    def display(self):
        for j in range(0, self.y):
            print()
        for i in range(0, self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        Rectangle.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        Rectangle.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        Rectangle.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        Rectangle.validator("y", value)
        self.__y = value
