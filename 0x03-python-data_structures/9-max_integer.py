#!/usr/bin/python3

def max_integer(my_list=[]):
    i = len(my_list)
    biggest = 0
    if (i == 0):
        return (None)
    for number in my_list:
        if (number > max):
            biggest = number
    return (biggest)
