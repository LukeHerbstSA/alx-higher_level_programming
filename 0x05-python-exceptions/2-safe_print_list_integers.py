#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    y = 0

    if (x == 0 or x < 0 or not my_list):
        print()
        return (0)
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            y += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return (y)
