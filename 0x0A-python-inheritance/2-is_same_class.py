#!/usr/bin/python3
"""
class type checker for passed objects or variables
"""


def is_same_class(obj, a_class):
    """
    function that checks the type of a passed object
    """
    if (isinstance(obj, a_class)):
        return (True)
