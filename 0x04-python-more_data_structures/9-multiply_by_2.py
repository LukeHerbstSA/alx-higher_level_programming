#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    copydic = a_dictionary.copy()
    for key in copydic:
        copydic[key] = copydic.get(key) * 2
    return(copydic)
