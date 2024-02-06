#!/usr/bin/python3
import json
"""
pedantic file documentation
"""


def to_json_string(my_obj):
    """
    converts string object into json
    """
    jsonobj = json.dumps(my_obj)
    return (jsonobj)
