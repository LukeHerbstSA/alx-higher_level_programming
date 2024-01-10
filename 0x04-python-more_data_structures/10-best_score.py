#!/usr/bin/python3

def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return (None)
    largest = 0
    for key in a_dictionary:
        keyval = a_dictionary.get(key)
        if (keyval > largest):
            largest = keyval
            largetoken = key
    return (largetoken)
