#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if (not isinstance(size, int)):
            print("size must be an integer")
            raise TypeError
        if (size < 0):
            print("size must be >= 0")
        self.position_checker(position)
        self.__size = size
        self.__position = position

    def position_checker(self, position):
        if (not isinstance(position, tuple) or len(position) != 2):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        for item in position:
            if (not isinstance(item, int) or item < 0):
                print("position must be a tuple of 2 positive integers")
                raise TypeError

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print("")
        for i in range(0, self.__size):
            for x in range(0, self.position[0]):
                print("-", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, size):
        if (not isinstance(size, int)):
            print("size must be an integer")
            raise TypeError
        if (size < 0):
            print("size must be >= 0")
            raise ValueError
        self.__size = size

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, position):
        self.position_checker(position)
        self.__position = position
