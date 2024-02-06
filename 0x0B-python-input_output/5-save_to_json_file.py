#!/usr/bin/python3
import json
"""
pedantic pedantic pedantic documentation
"""


def save_to_json_file(my_obj, filename):
    """
    changes my_obj to json version then writes to filename
    """
    newobj = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as myfile:
        myfile.write(newobj)
