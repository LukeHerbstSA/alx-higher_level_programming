#!/usr/bin/python3
"""
lookup module function to make attribute object
"""
def lookup(obj):
    """
    returns a list object from passed class obj
    """
    return (dir(obj))
