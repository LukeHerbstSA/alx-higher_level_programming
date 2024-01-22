#!/usr/in/python3

def safe_function(fct, *args):
    result = None

    try:
        result = fct(args[0], args[1])
    except Exception as ex:
        print("Exception: ", ex)
    return (result)
