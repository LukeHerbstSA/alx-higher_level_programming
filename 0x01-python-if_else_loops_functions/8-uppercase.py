#!/usr/bin/python3
def isupper(str):
    string = list(str)
    for i in range(0, len(string)):
        if (ord(string[i]) >= 97 and ord(string[i]) <= 123):
            string[i] = chr(ord(string[i]) - 32)
    string = "".join(string)
    print(string)
