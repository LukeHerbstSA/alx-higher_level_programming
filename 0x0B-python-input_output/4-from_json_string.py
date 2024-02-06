#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""
import json


def from_json_string(my_str):
    """
    changes json string into object
    """
    newobj = json.loads(my_str)
    return (newobj)
