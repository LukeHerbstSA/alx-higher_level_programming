#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    print(i, end=" ")
    if (i == 0 or i > 1):
        print("arguments", end="")
    else:
        print("argument", end="")
    if (i == 0):
        print(".")
    else:
        print(":")
    for j in range(1, i):
        print("{}:".format(j), "{}".format(sys.argv[j]))
