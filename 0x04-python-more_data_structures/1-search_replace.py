#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newlist = []

    if (my_list is None):
        return (None)
    if (len(my_list) == 0):
        return (my_list)
    for i in range(0, len(my_list)):
        if (my_list[i] == search):
            newlist.append(replace)
        else:
            newlist.append(my_list[i])
    return (newlist)
