#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    sum = 0

    for j in range(1, i):
        sum = sum + int(sys.argv[j])
    print(sum)
