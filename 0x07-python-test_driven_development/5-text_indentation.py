#!/usr/bin/python3

def text_indentation(text):
    symbols = ["?", ":", "."]
    j = 0

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for char in text:
        if (char == " " and j == 0):
            pass
        else:
            j = 1
            print(char, end="")
            if (char in symbols):
                j = 0
                print("\n")
            if char == "\n":
                j = 0
