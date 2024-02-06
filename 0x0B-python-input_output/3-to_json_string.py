#!/usr/bin/python3
import json
"""
pedantic file documentation
"""


def to_json_string(my_obj):
    """
    converts string object into json
    """
    strobj = json.loads(my_obj)
    return (strobj)
