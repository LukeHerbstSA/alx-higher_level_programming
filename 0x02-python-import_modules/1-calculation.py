#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{} +".format(a), "{} =".format(b), "{}".format(add(a, b)))
    print("{} -".format(a), "{} =".format(b), "{}".format(sub(a, b)))
    print("{} x".format(a), "{} =".format(b), "{}".format(mul(a, b)))
    print("{} /".format(a), "{} =".format(b), "{}".format(div(a, b)))

