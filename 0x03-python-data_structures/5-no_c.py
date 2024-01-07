#!/usr/bin/python3

def no_c(my_string):
    bad_chars = ["c", "C"]
    newstring = ""
    j = 0
    for i in range(0, len(my_string)):
        if (my_string[i] not in bad_chars):
            newstring[j] = my_string[i]
            j = j + 1
    return (newstring)
