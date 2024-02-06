#!/usr/bin/python3
"""
pedantic docstring documentation
"""


def write_file(filename="", text=""):
    """
    writes passed text to filename
    """
    with open(filename, "w+", encoding="utf-8") as myfile:
        chars = myfile.write(text)
    return (chars)
