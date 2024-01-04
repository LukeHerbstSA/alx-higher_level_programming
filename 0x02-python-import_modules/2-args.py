#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    print(i - 1, end=" ")
    if (i == 1 or i > 2):
        print("arguments", end="")
    else:
        print("argument", end="")
    if (i == 1):
        print(".")
    else:
        print(":")
    for j in range(1, i):
        print("{}:".format(j), "{}".format(sys.argv[j]))
