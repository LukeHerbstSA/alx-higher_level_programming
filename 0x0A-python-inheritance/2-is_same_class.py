#!/usr/bin/python3
"""
class type checker for passed objects or variables
"""


def is_same_class(obj, a_class):
    """
    function that checks the type of a passed object
    """
    if (type(obj) is a_class):
        return (True)
    else:
        return (False)
