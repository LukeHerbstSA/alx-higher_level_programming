#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    y = 0

    if (x == 0 or x < 0 or not my_list):
        return (y)
    for element in my_list[:x - 1]:
        try:
            print("{:d}".format(element), end="")
            y += 1
        except ValueError:
            pass
    print()
    return (y)
