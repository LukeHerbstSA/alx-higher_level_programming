#!/usr/bin/python3

if __name__ == "__main__":
    def element_at(my_list, idx):
        i = len(my_list)

        if (idx < 0 or idx >= i):
            return (None)
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
