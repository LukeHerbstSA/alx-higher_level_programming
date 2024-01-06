#!/usr/bin/python3

if __name__ == "__main__":
    def new_in_list(my_list, idx, element):
        i = len(my_list)

        copy_list = my_list.copy()
        if (idx < 0 or idx >= i):
            return (None)
        copy_list[idx] = element
        return (copy_list)
