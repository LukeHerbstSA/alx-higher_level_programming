#!/usr/bin/python3
"""
pedantic pedantic pedantic documentation
"""


class Student:
    """
    student class with init and to_json functionality
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        return (vars(self))
