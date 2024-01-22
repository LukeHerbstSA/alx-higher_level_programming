#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    y = 0

    if (x == 0 or x < 0 or my_list is None):
        return (y)
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            y += 1
        except IndexError:
            break
    print()
    return (y)
