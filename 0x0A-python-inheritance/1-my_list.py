#!/usr/bin/python3
"""
module to create a list instance using a class
"""


class MyList(list):
    """
    class my list that initializes self with list & cls behaviour
    """
    def __init__(self):
        super().__init__()
    def print_sorted(self):
        print(sorted(self))
