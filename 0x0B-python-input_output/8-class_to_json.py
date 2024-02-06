#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""


def class_to_json(obj):
    """
    returns dictionary representation of an object simplified
    """
    newobj = obj.dumps(obj)
    newobj = newobj.loads(obj)
    return (newobj)
