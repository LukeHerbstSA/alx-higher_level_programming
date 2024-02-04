#!/usr/bin/python3
"""
simple locked class
"""


class LockedClass:
    """
    locked class that prevents new instance attributes being added
    """
    def __slots__("first_name")
    def __init__(self, name):
        self.first_name = name
