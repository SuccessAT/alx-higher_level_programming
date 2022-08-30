#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)

    int_max = my_list[0]

    for i in range(1, length):
        if my_list[i] > int_max:
            int_max = my_list[i]

    return (int_max)
