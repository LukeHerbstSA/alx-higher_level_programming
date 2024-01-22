#!/usr/bin/python3

def safe_print_division(a, b):
    sum = 0

    try:
        sum = a / b
    except ZeroDivisionError:
        sum = None
    finally:
        if sum is not None:
            print("Inside Result: {:.1f}".format(sum))
        else:
            print("Inside Result: {}".format(None))
    return (sum)
