#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp_list = set(my_list)
    number = 0

    for i in temp_list:
        number += i

    return (number)
