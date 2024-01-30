#!/usr/bin/python3

"""
print square module
"""


def print_square(size):
    """
    print_square class
    """
    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        if (i != size - 1):
            print()
