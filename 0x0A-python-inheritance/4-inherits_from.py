#!/usr/bin/python3
"""
inheritance and subclass checking
"""


def inherits_from(obj, a_class):
    """
    checks if obj is indirectly or directly sub of a_class
    """
    if (not isinstance(obj, a_class) and issubclass(type(obj), a_class)):
        return (True)
    else:
        return (False)
