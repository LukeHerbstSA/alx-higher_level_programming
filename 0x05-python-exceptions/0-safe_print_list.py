#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    y = 0

    if (x == 0 or x < 0 or my_list is None):
        return (y)
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            y += 1
    except IndexError:
        return (y)
    except TypeError:
        return (y)
    finally:
        print()
    return (y)
