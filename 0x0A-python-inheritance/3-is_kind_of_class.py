#!/usr/bin/python3
"""
class type checker with passed objects
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class checks obj to see if it is an instance of a_class or sub
    """
    if (isinstance(obj, a_class) or issubclass(type(obj), a_class)):
        return (True)
    else:
        return (False)
