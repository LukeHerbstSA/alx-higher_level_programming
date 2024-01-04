#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{:d} +".format(a), "{:d} =".format(b), "{:d}".format(add(a, b)))
