#!/usr/bin/python3
"""Module rectangle inherits from base."""
Base = __import__("base").Base


class Rectangle(Base):
    """Class Rectangle - inherits from rectangle."""

    def __str__(self):
        """Return str repr of instance."""
        firsthlf = "[Rectangle] ({}) {}/{} ".format(self.id, self.x, self.y)
        scndhlf = "- {}/{}".format(self.width, self.height)
        return(firsthlf + scndhlf)

    @staticmethod
    def validator(*values):
        """Validate passed list of values."""
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
        """Initialize rectangle instances."""
        Rectangle.validator(["width", width, "height", height, "x", x, "y", y])
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def to_dictionary(self):
        """Return dict repr of self."""
        return (self.__dict__)

    def update(self, *args, **kwargs):
        """Update current instance."""
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
        """Display instance visually."""
        for j in range(0, self.y):
            print()
        for i in range(0, self.__height):
            print(" " * self.x, end="")
            print("#" * self.__width)

    @property
    def width(self):
        """Return width of instance."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set width value of instance."""
        Rectangle.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Return height of instance."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set height of instance."""
        Rectangle.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Return x of instance."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set x co ord of instance."""
        Rectangle.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Return y co ord of instance."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set y co ord of instance."""
        Rectangle.validator("y", value)
        self.__y = value
