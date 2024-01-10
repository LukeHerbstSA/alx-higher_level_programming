#!/usr/bin/python3

def uniq_add(my_list=[]):
    if (my_list is None):
        return (None)
    if (len(my_list) is == 0):
        return (my_list)
    setlist = set(my_list)
    sum = 0

    for element in setlist:
        sum = sum + element
    return (sum)
