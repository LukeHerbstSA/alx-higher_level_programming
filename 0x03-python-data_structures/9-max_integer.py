#!/usr/bin/python3

def max_integer(my_list=[]):
    if (my_list is None):
        return (None)
    i = len(my_list)
    if (i == 0):
        return (None)
    biggest = my_list[0]
    for number in my_list:
        if (number > biggest):
            biggest = number
    return (biggest)
