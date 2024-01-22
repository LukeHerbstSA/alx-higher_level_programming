#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    i = 0

    for i in range(0, list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return (new_list)
