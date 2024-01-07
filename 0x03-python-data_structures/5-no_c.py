#!/usr/bin/python3

def no_c(my_string):
    bad_chars = ["c", "C"]
    strcopy = my_string.copy()
    for char in bad_chars:
        while (char in strcopy):
            strcopy.remove(char)
    return (strcopy)
