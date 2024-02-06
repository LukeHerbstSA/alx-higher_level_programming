#!/usr/bin/python3
"""
pedantic docstring documentation for read_file
"""


def read_file(filename=""):
    """
    opens file filename and reads everything, then prints
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read())
