#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""


class Student:
    """
    student class with init and to_json functionality
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (isinstance(attrs, list) and len(attrs) > 0):
            mydict = vars(self)
            newdict = {}
            for key in mydict:
                if (key in attrs):
                    newdict[key] = mydict[key]
            return (newdict)
        else:
            return (vars(self))
