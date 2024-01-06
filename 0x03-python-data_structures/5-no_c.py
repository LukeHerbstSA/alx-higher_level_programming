#!/usr/bin/python3

if __name__ == "__main__":
    def no_c(my_string):
        bad_chars = ["c", "C"]
        strcopy = my_string.copy()
        j = len(strcopy)
        for i in range(-1, j * -1, -1):
            for char in bad_chars:
                if (strcopy[i] == char):
                    strcopy.remove(char)
        return (strcopy)
