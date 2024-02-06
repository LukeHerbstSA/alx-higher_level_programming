#!/usr/bin/python3
"""
pedantic file documentation
"""


def append_write(filename="", text=""):
    """
    function appends text to end of filename
    """
    with open(filename, "a+", encoding="utf-8") as myfile:
        chars = myfile.write(text)
    return (chars)
