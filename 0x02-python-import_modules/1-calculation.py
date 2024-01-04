#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{:d} +".format(a), "{:d} =".format(b), "{:d}".format(add(a, b)))
    print("{:d} -".format(a), "{:d} =".format(b), "{:d}".format(sub(a, b)))
    print("{:d} x".format(a), "{:d} =".format(b), "{:d}".format(mul(a, b)))
    print("{:d} /".format(a), "{:d} =".format(b), "{:d}".format(div(a, b)))
