#!/usr/bin/python3

"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        largest = rect_2 if rect_2.area > rect_1.area else rect_1
        return (largest)

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

    def __str__(self):
        result = ""
        if (self.__width == 0 or self.__height == 0):
            return (result)
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                if (self.print_symbol == ""):
                    result = result + "{}".format(Rectangle.print_symbol)
                else:
                    result = result + "{}".format(self.print_symbol)
            if (i != self.__height - 1):
                result = result + "\n"
        return (result)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        Rectangle.heightcheck(height)
        Rectangle.widthcheck(width)
        self.__width = width
        self.__height = height
        self.print_symbol = ""
        Rectangle.number_of_instances += 1

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
