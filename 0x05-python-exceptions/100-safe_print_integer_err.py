#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    boolvar = True

    try:
        print("{:d}".format(value))
    except Exception as ex:
        boolvar = False
        print("Exception: {}".format(ex), file=sys.stderr)
    return boolvar
