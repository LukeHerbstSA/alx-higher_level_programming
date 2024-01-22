#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    y = 0

    if (x == 0 or my_list is None):
        return (y)
    try:
        for element in my_list:
            if (y == x):
                break
            print(element, end="")
            y += 1
        if (y < x):
            print()
            raise IndexError
    except IndexError:
        return (y)
    print()
    return (y)
