#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    j = len(my_list)
    if (j == None or j == 0):
        return (None)
    for i in range(-1, j * -1 - 1, -1):
        print("{:d}".format(my_list[i]))
