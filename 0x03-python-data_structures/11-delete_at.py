#!/usr/bin/python3

def delete_at(my_list, idx=0):
    if (my_list is None):
        return (my_list)
    length = len(my_list)
    if (length == 0):
        return (my_list)
    if (idx < 0 or idx >= length):
        return (my_list)
    my_list[:] = my_list[:idx] + my_list[idx + 1:]
    new_list = my_list.copy()
    return (new_list)
