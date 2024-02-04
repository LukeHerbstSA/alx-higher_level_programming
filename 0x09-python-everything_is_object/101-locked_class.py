#!/usr/bin/python3

"""
simple locked class

Example usage:

    obj = LockedClass("james")
    obj.first_name = "franco"
"""


class LockedClass:
    """
    locked class that prevents new instance attributes being added

    only allows attribute first name to be changed
    """
    def __slots__ = "first_name"

    def __init__(self, name):
        """
        pedantic init documentation
        """
        self.first_name = name
