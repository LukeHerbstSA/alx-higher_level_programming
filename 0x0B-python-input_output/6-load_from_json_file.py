#!/usr/bin/python3
import json
"""
pedantic pedantic pedantic pedantic
"""


def load_from_json_file(filename):
    """
    opens filename, loads the json obj into its regular version
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        newobj = filename.read()
    newobj = json.loads(newobj)
    return (newobj)
