#!/usr/bin/python3
""" modules with one class, Square
"""


class Square:
    """ defines instances of class Square
    """
    def __init__(self, size):
        """ initializer function for instantiations of Square

        Args:
            param1 (int): passed size of Square
        """
        self.__size = size
