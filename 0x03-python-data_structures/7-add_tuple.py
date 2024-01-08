#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if (tuple_a is None):
        tuple_a = ()
    if (tuple_b is None):
        tuple_b = ()

    a_len = len(tuple_a)
    b_len = len(tuple_b)
    val0 = 0 if a_len == 0 else tuple_a[0]
    val1 = 0 if b_len == 0 else tuple_b[0]
    val2 = 0 if a_len == 1 else tuple_a[1]
    val3 = 0 if b_len == 1 else tuple_b[1]
    new_tuple = (val0 + val1, val2 + val3)
    return (new_tuple)
