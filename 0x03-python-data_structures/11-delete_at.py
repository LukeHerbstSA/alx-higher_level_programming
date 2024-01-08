#!/usr/bin/python3

if __name__ == "__main__":
    def delete_at(my_list=[], idx=0):
        length = len(my_list)
        if (idx < 0 or idx >= length):
            return (my_list)
        my_list = my_list[:idx] + my_list[idx + 1:]
        return (my_list)
