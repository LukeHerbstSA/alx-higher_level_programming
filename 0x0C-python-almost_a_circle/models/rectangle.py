#!/usr/bin/python3
Base = __import__("base.py").Base

class Rectangle(Base):
    def __str__(self):
        out = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y. self.__width, self.__height)
        return (out)

    @staticmethod
    def validator(*values):
        for i in range(0, len(values)):
            if (i % 2 != 0):
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

    def update(self, *args):
        for i in range(0, len(args)):
            if (i == 0): # switch case?
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

    @property.setter
    def width(self, value):
        validator("width", value)
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @property.setter
    def height(self, value):
        validator("height", value)
        self.__height = value

    @property
    def x(self):
        return (self.__x)
    @property.setter
    def x(self, value):
        validator("x", value)
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @property.setter
    def y(self, value):
        validator("y", value)
        self.__y = value
