#!/usr/bin/python3
import json
"""
pedantic pedantic pedantic documentation
"""


def from_json_string(my_str):
    """
    changes json string into object
    """
    newobj = json.loads(my_str)
    return (newobj)
